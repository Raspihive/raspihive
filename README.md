   ![](/assets/Logo/TheHive.png)


![PyPI](https://img.shields.io/pypi/v/raspihive?style=for-the-badge) ![PyPI - Status](https://img.shields.io/pypi/status/raspihive?style=for-the-badge) ![PyPI - Downloads](https://img.shields.io/pypi/dw/raspihive?style=for-the-badge) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/raspihive?style=for-the-badge)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/raspihive/raspihive?style=for-the-badge) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/raspihive/raspihive?style=for-the-badge) ![GitHub issues](https://img.shields.io/github/issues-raw/raspihive/raspihive?style=for-the-badge) ![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/raspihive/raspihive?style=for-the-badge) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/raspihive/raspihive?style=for-the-badge) 

![GitHub](https://img.shields.io/github/license/raspihive/raspihive?style=for-the-badge) ![GitHub contributors](https://img.shields.io/github/contributors/raspihive/raspihive?style=for-the-badge) 

# Install


### Install from pypi:
`pip install raspihive`


### Install from source:

# Setup

if you want to run RaspiHive on Raspberry Pi OS, you need the 64 Bit version (wich is Beta at the moment).

download the Image from:
[Raspberry Pi 64 Bit Beta OS](https://downloads.raspberrypi.org/raspios_arm64/images/raspios_arm64-2020-05-28/2020-05-27-raspios-buster-arm64.zip)

and use the Raspberry Pi imager to write it on a SD Card: 

[Raspberry Pi Downloads](https://www.raspberrypi.org/downloads/)

Tested on Ubuntu 18.04.

1. Install SetupTools:

```
$ sudo apt-get install python3-setuptools
```

2. Clone this repo:
```
$ git clone https://github.com/raspihive/raspihive.git
```

3. Install `raspihive` Python3 module:
```
$ cd raspihive
$ sudo python3 setup.py install
```

---
---
# Development

If you are interested in contributing, please go through our [CONTRIBUTING](CONTRIBUTING.md) guidelines first.

### Setup

#### Environment
- Setup virtualenv: `python3 -m venv venv`
- Activate venv: `source venv/bin/activate`

#### Dependencies
`pip3 install -r requirements/dev.txt`

### Run
`python3 -m raspihive`


---
__Works on__:

- [x] Ubuntu 18.04
- [x] Ubuntu 20.04
- [x] Fedora 33
- [x] LinuxMint 20

Development screenshots: 

   ![](/assets/Logo/raspihive0.png)
