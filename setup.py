#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup
import kansuji2num

setup(
    name='kansuji2num',
    version=kansuji2num.__version__,
    license='MIT',
    description='converts kansuji in the given string to number',
    author='tetutaro',
    author_email='tetsutaro.maruyama@gmail.com',
    url='https://github.com/tetutaro/kansuji2num',
    packages=['kansuji2num']
)
