   ![](/assets/Logo/TheHive.png)

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
`sudo python3 raspihive/raspihive.py`

---
__Works on__:

- [x] Ubuntu 18.04
- [x] Ubuntu 20.04
- [ ] Fedora 22
