# coding:utf-8
import unittest, os
import HTMLTestRunner
from common.emailUtil import MyEmail


class Case01(unittest.TestCase):

    def setUp(self):
        print('lalala')
    """test class description"""
    def test_111(self):
        """测试test_111的功能"""

        self.assertEqual(1,2,"assert error --")

    # @unittest.skip('skip anyway')
    def test_112(self):
        self.assertEqual(1,1,"aaa")


