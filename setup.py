#!/usr/bin/env python
import os
from setuptools import setup, find_packages

def get_version(version_tuple):
    if not isinstance(version_tuple[-1], int):
        return '.'.join(
            map(str, version_tuple[:-1])
        ) + version_tuple[-1]
    return '.'.join(map(str, version_tuple))

# path to the packages __init__ module in project source tree
init = os.path.join(os.path.dirname(__file__), 'spawner','__init__.py')
version_line = list(filter(lambda l: l.startswith('VERSION'), open(init)))[0]
PKG_VERSION = get_version(eval(version_line.split('=')[-1]))

setup(
    name="spawner-module",
    version="1.0",
    description='Python Module to Spawn compute on Cloud',
    author='sachin'
    author_email='sachin@netbook.ai',
    license="license",
    url='https://github.com/NetBook-ai/spawner-module',
    packages=find_packages('spawner'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)"
    ] 
)