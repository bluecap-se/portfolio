# Portfolio

![Status](https://img.shields.io/badge/status-stable-brightgreen.svg)
![PyPI - Python Version](https://img.shields.io/badge/python-3.7-blue.svg)
![Platform](https://img.shields.io/badge/platform-win%20%7C%20lin%20%7C%20osx-lightgrey.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)


## Install

### Install from source

This project relies on [Pipenv](https://docs.pipenv.org/), ensure that it is installed with `pip3 install pipenv` first.

```
$ git clone git@github.com:bluecap-se/portfolio.git
$ cd portfolio
$ pipenv install --three
$ pipenv shell
```

## Usage

Run the webserver with:

```bash
$ python wsgi.py

```

### Local testing

```bash
$ python wsgi.py --config local

```

### Production

```bash
$ python wsgi.py --config prod

```

## License

Published under [MIT License](https://github.com/bluecap-se/portfolio/master/LICENSE).
