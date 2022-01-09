# digic
 
A privacy focused command line tool to track your crypto portfolio.

## What is digic?

Digic is an open source command line tool written in Python to 
track your crypto portfolio. Currently, it supports Bitcoin and
Ethereum addresses.

## Installation

### Using pipx (recommended)

[PIPX](https://github.com/pypa/pipx) creates a virtual environment for each 
package, while also ensuring that its applications are accessible through
a directory that is on your `$PATH`. This allows each package to be 
upgraded or uninstalled without causing conflicts with other packages, 
and allows you to safely run the applications from anywhere. More info:
- [PIPX Github](https://github.com/pypa/pipx)
- [Packaging Python](https://packaging.python.org/en/latest/guides/installing-stand-alone-command-line-tools/)

#### Install PIPX

##### On macOS

```bash
brew install pipx
pipx ensurepath
```

##### On Linux, install via pip (requires pip 19.0 or later)

```bash
python3 -m pip install --user pipx
python3 -m pipx ensurepath
```

##### On Windows, install via pip (requires pip 19.0 or later)

```bash
# If you installed python using the app-store, replace `python` with 
# `python3` in the next line.
python -m pip install --user pipx
```

It is possible (even most likely) the above finishes with a WARNING looking 
similar to this:

```bash
WARNING: The script pipx.exe is installed in `<USER folder>\AppData\
Roaming\Python\Python3x\Scripts` which is not on PATH
```

If so, go to the mentioned folder, allowing you to run the pipx executable
directly. Enter the following line (even if you did not get the warning):

```bash
pipx ensurepath
```

This will add both the above-mentioned path and the 
`%USERPROFILE%.local\bin` folder to your search path. Restart your 
terminal session and verify `pipx` does run.

#### Install digic

```bash
pipx install digic
```

Check if digic is correctly installed

```bash
digic --help
```

## Privacy

Digic works locally, which means that your public addresses are
stored locally in your computer. We do not use any server to
store them. 

## How does Digic get blockchain data?

I use two main public APIs to retrieve blockchain data, and one
to fetch crypto prices.

### Blockchain APIs

1. https://etherscan.io
2. https://blockchain.com

### Crypto prices API

1. https://coingecko.com

In order to use Digic, you must create an API key in etherscan.io.
You can sign up [here](https://etherscan.io/login).    
The other APIs are public (without key).

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


