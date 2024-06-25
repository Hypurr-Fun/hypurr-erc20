# HL-ERC20

A bare-bones implementation of the Ethereum [ERC-20 standard](https://eips.ethereum.org/EIPS/eip-20), written in [Solidity](https://github.com/ethereum/solidity).

For binding with a hyperliquid spot asset

## Basic Use

### Set parameters in deploy script
```python
rpc_url = "https://api.hyperliquid-testnet.xyz/evm"
deployed_contract_address = None
token_id = "0xc14f993cb5ad363118704e783b0dddc9"
token_name = "Test Token"
```


### Initialize poetry
```bash
poetry install
```

### Enter shell
```bash
poetry shell
```

### Add hyperliquid testnet
```bash
brownie networks add Hyperliquid testnet host=https://api.hyperliquid-testnet.xyz/evm chainid=998
```

### Add hyperliquid account
```bash
brownie accounts new hl-testnet
```

### Deploy
```bash
brownie run deploy --network testnet
```