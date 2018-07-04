import logging
from datetime import datetime
from common import readConfig
import os
import threading, time

localReadConfig = readConfig.ReadConfig()

class Logger:
    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        # console_level = localReadConfig.get_log_level("console_level")
        # print(type(logging.DEBUG))
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
        log_path = os.path.dirname(os.getcwd()) + '/Logs/'
        if not os.path.exists(log_path):
            os.mkdir(log_path)
        log_name = log_path + 'output.log'
        # log_name = log_path + rq + '.log'

        fh = logging.FileHandler(log_name)
        fh.setLevel(logging.DEBUG)

        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s')
        # formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger

# if __name__ == '__main__':
#     logger = Logger("log.py").getlog()
#     logger.info("aaa")
#     logger.error("error message")
#     logger.debug("debug message")
