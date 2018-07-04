# coding:utf-8
import unittest, os
import HTMLTestRunner
from common.emailUtil import MyEmail
from testCases.case01 import Case01
from testCases.case02 import Case02

if __name__ == '__main__':


    suite = unittest.TestSuite()
    suite.addTest(Case01("test_111"))
    suite.addTest(Case01("test_112"))
    suite.addTest(Case02("test_1122"))
    log_path = os.path.split(os.path.realpath(__file__))[0]
    print(log_path)
    fp = open(log_path+'/result1.html', 'wb')
    # fp = open('result1.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='some test', description='部分测试用例', verbosity=2)
    runner.run(suite)

    # email = MyEmail.get_email()
    # email.send_email()

    fp.close()


    suite = unittest.TestSuite()
    tests = [Case01("test_111"), Case01("test_112"), Case02("test_1122")]
    suite.addTests(tests)
    fp = open('result1.html', 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='some test', description='部分测试用例', verbosity=2)
    runner.run(suite)
    fp.close()

