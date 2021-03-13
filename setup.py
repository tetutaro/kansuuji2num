#!/usr/bin/env python
# -*- coding:utf-8 -*-
from setuptools import setup
import kansuji2num

setup(
    name='kansuji2num',
    version=kansuji2num.__version__,
    license='MIT',
    description='convert kansuji in the given text to arabic numerals',
    author='tetutaro',
    author_email='tetsutaro.maruyama@gmail.com',
    url='https://github.com/tetutaro/kansuji2num',
    entry_points={
        'console_scripts': [
            'kansuji2num = kansuji2num:main',
        ],
    },
    packages=[
        'kansuji2num'
    ],
    test_suite='tests.suite'
)
