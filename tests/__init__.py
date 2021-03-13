#!/usr/bin/env python
# -*- coding:utf-8 -*-
from unittest import TestSuite, makeSuite
from .test_kansuji2num import TestKansuji2num


def suite() -> TestSuite:
    suite = TestSuite()
    suite.addTests(makeSuite(TestKansuji2num))
    return suite
