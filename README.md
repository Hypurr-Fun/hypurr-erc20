# HL-ERC20

A bare-bones implementation of the Ethereum [ERC-20 standard](https://eips.ethereum.org/EIPS/eip-20), written in [Solidity](https://github.com/ethereum/solidity).

For binding with a hyperliquid spot asset

Configure your target token and

## Basic Use


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