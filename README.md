   ![](/assets/Logo/TheHive.png)

# Setup

if you want to run RaspiHive on Raspberry Pi OS, you need the 64 Bit version (wich is Beta at the moment).

download the Image from:
[Raspberry Pi 64 Bit Beta OS](https://downloads.raspberrypi.org/raspios_arm64/images/raspios_arm64-2020-05-28/2020-05-27-raspios-buster-arm64.zip)

and use the Raspberry Pi imager to write it on a SD Card: 

[Raspberry Pi Downloads](https://www.raspberrypi.org/downloads/)

# Install

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

### Setup
Currently, we need to sudo access to access system password. So, you'll have to install the packages system wide.

#### Dependencies `sudo pip install guizero tk`

### Run
`sudo python3 raspihive.py`

---
__Works on__:

- [x] Ubuntu 18.04
- [x] Ubuntu 20.04
- [ ] Fedora 22
