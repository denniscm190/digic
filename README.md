# digic
 
A privacy focused command line tool to track your crypto portfolio.

## Installation

*If you need a more comprehensive explanation. Follow this [guide](https://docs.digic.app/non-techies/what-is-digic).*

First, install Python. To do so, go to [python.org](https://www.python.org/downloads/) and download 
the latest version for your operating system.

### Using pipx (recommended)

Next, install PIPX. [PIPX](https://github.com/pypa/pipx) creates a virtual environment for each package, while also 
ensuring that its applications are accessible through a directory that is on your `$PATH`. This allows each package to 
be upgraded or uninstalled without causing conflicts with other packages, and allows you to safely run the applications 
from anywhere. More info:
- [PIPX Github](https://github.com/pypa/pipx)
- [Packaging Python](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/)

#### Install PIPX

To install PIPX follow this [guide](https://github.com/pypa/pipx#install-pipx).

#### Install digic

Finally, we can install Digic safely using PIPX.

```bash
pipx install digic
```

Check if digic is correctly installed.

```bash
digic --help
```

## Usage

Check the [documentation](https://docs.digic.app) for more information.

## Privacy

Digic works locally, which means that your public addresses are stored locally in your computer. We do not use any 
server to store them. 

## How does Digic get blockchain data?

Digic uses the following APIs to retrieve blockchain data and crypto prices.

1. https://etherscan.io
2. https://blockchain.com
3. https://coingecko.com

## Development

I spent some time looking for solutions to track my crypto portfolio. There are many in the market, but I do not trust
them. Most of them store my public keys in servers, and others require some kind of registration to link my public keys 
to my identity. In order to avoid this, I've created Digic.

The idea is to create a program that runs locally, and does not depend on any server or centralized API. This will be 
implemented gradually in future versions.

If you like Digic, please consider becoming a contributor. I need help to improve it.

### Roadmap
- [x] Release beta `0.0.1`.
- [ ] Add command to check the transactions of each wallet.
- [ ] Add command to check the balance of all the address at a glance.
- [ ] Support Avalanche blockchain.
- [ ] Find a solution to stop depending on centralized APIs.


