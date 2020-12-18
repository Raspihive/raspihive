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

#### Environment
- Setup virtualenv: `python3 -m venv venv`
- Activate venv: `source venv/bin/activate`

#### Dependencies
`pip install -r requirements/dev.txt`

### Run
`python -m raspihive`


---
__Works on__:

- [x] Ubuntu 18.04
- [x] Ubuntu 20.04
- [x] Fedora 33
