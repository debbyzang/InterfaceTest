# coding:utf-8
import unittest

class Case02(unittest.TestCase):
    def setUp(self):
        print('setup ====')

    def setUpClass(cls):
        print('setUpClass ====')

    def tearDown(self):
        print('tearDown ===')

    def tearDownClass(cls):
        print('tearDownClass ====')

    def test_1122(self):
        self.assertEqual(1,2,"assert error --")

    def test_1234(self):
        self.assertEqual(1,3,"aaa")