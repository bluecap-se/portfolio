#!/usr/bin/env python

from setuptools import setup


VERSION = '1.1'

setup(
    name='portofolio',
    version=VERSION,
    author='jdi',
    install_requires=[
        'flask==0.10',
        'jinja2==2.7',
        'flask-assets==0.8',
        'flask-debugtoolbar',
        'configobj',

        'closure',
        'cssmin'
    ]
)
