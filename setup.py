#!/usr/bin/env python

import os
import sys

from setuptools import setup

os.chdir(os.path.dirname(sys.argv[0]) or ".")

try:
    long_description = open("README.rst", "U").read()
except IOError:
    long_description = "See https://github.com/joaonc/pprintpp2"

setup(
    name="pprintpp",
    version="0.4.0",
    url="https://github.com/joaonc/pprintpp2",
    author="David Wolever",
    author_email="david@wolever.net",
    description="A drop-in replacement for pprint that's actually pretty",
    long_description=long_description,
    packages=["pprintpp"],
    entry_points={
        'console_scripts': [
            'pypprint = pprintpp:console',
        ],
    },
    install_requires=[],
    license="BSD",
    classifiers=[
        x.strip()
        for x in """
            Environment :: Console
            Intended Audience :: Developers
            License :: OSI Approved :: BSD License
            Natural Language :: English
            Operating System :: OS Independent
            Programming Language :: Python
            Programming Language :: Python :: 3
            Topic :: Software Development
            Topic :: Utilities
        """.split(
            "\n"
        )
        if x.strip()
    ],
)
