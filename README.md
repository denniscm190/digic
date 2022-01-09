# digic
 
A privacy focused command line tool to track your crypto portfolio.

## What is digic?

Digic is an open source command line tool written in Python to 
track your crypto portfolio. Currently, it supports Bitcoin and
Ethereum addresses.

## Privacy

Digic works locally, which means that your public addresses are
stored locally in your computer. We do not use any server to
store them. 

## How does Digic get blockchain data?

We use two main public APIs to retrieve blockchain data, and one
to fetch crypto prices.

### Blockchain APIs

1. https://etherscan.io
2. https://blockchain.com

### Crypto prices API

1. https://coingecko.com

In order to use Digic you must create an API key in etherscan.io.
You can sign up [here](https://etherscan.io/login). The other 
APIs are public (without key).

## Development

I spent some time searching for solutions to track my crypto
portfolio. There are many in the market, but I do not trust them. 
Most of them store my public keys in servers and others
require some kind of registration process to link my public 
keys to my identity. For this reason, I created Digic.

If you like Digic please consider becoming a contributor. I need
help to improve it.

### Roadmap
- [ ] Get contributors to the project
- [ ] Support for Avalanche blockchain
- [ ] Support multiple user accounts
- [ ] Find a solution to stop depending on centralized APIs


