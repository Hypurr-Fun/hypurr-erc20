#!/usr/bin/python3

from brownie import HLERC20, accounts
import requests
from eth_account import Account
from eth_account.signers.local import LocalAccount
from web3 import Web3
from web3.middleware import construct_sign_and_send_raw_middleware
from hyperliquid.utils import constants
from hyperliquid.utils.signing import get_timestamp_ms, sign_l1_action, address_to_bytes
from hyperliquid.info import Info


rpc_url = "https://api.hyperliquid-testnet.xyz/evm"
deployed_contract_address = "0xC0a1eD135B3aBBAcF12851bACc96A2649A50bA58"
token_id = "0xc14f993cb5ad363118704e783b0dddc9"

def main():
    accounts.load("hl-testnet")
    # Get token supply by calling token Info
    account = accounts[0]
    # Create a Web3 account using the private key
    web3_account = Web3().eth.account.from_key(account.private_key)

    info = Info(constants.TESTNET_API_URL)
    spot_meta = info.spot_meta()
    token = None
    for t in spot_meta['tokens']:
        if t['tokenId'] == token_id:
            token = t
            break

    if token is None:
        raise Exception("Token not found")

    token_details = info.token_details(token_id)
    max_supply = float(token_details['maxSupply'])
    wei_decimals = int(token['weiDecimals'])
    # our contract will have 18 decimals by default
    evm_decimals = 18
    # compute total supply in big int
    total_supply = int(max_supply * (10 ** (evm_decimals)))

    if deployed_contract_address is None:
        contract = HLERC20.deploy("Test Token", token.Name, total_supply, evm_decimals, {'from': account})
        contract_address = contract.address
    else:
        contract_address = deployed_contract_address

    contract_address = contract_address.lower()
    token_index = int(token['index'])
    action = {
          "type": "spotDeploy",
          "setEvmContract": {
              "token": token_index,
              "address": contract_address,
              "evmExtraWeiDecimals": evm_decimals - wei_decimals,
          },
      }
    nonce = get_timestamp_ms()
    signature = sign_l1_action(web3_account, action, None, nonce, False)
    payload = {
      "action": action,
      "nonce": nonce,
      "signature": signature,
      "vaultAddress": None,
    }
    print(payload)
    response = requests.post(constants.TESTNET_API_URL + "/exchange", json=payload)
    print(response.json())