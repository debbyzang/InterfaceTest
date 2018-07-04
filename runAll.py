# coding:utf-8
import unittest, os
import HTMLTestRunnerCN
# import HTMLTestRunner
from common.emailUtil import MyEmail

suite = unittest.TestSuite()  # 创建测试套件
# 找到某个目录下所有的以case开头的Python文件里面的测试用例
log_path = os.path.split(os.path.realpath(__file__))[0] + '/testCases/'
all_cases = unittest.defaultTestLoader.discover(log_path, 'case*.py')
for case in all_cases:
    suite.addTests(case)  # 把所有的测试用例添加进来
fp = open('result.html', 'wb')
# runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='all_tests', description='所有测试情况', verbosity=2)
runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=fp, title='all_tests', description='所有测试情况', verbosity=2)
runner.run(suite)
email = MyEmail.get_email()
email.send_email()



