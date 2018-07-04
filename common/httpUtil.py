import requests
from common import readConfig
import json
from common.log import Logger
from urllib import parse, request

localReadConfig = readConfig.ReadConfig()


class ConfigHttp:

    def __init__(self):
        self.host = localReadConfig.get_http("baseurl")
        self.port = localReadConfig.get_http("port")
        self.timeout = localReadConfig.get_http("timeout")
        self.logger = Logger("httpUtil.py").getlog()

    # defined http get method
    def get(self, url, param=None):
        new_url = self.host + ":" + self.port + "/" + url
        header = {'Content-Type': 'application/json'}
        try:
            if param != None:
                textmod = parse.urlencode(param)
                req = request.Request(url='%s%s%s' % (new_url, '?', textmod), headers=header)
                self.logger.debug('%s%s%s' % (new_url, '?', textmod))
            else:
                req = request.Request(url='%s' % (new_url), headers=header)
                self.logger.debug(new_url)
            res = request.urlopen(req)
            res = res.read()
            hjson = json.loads(res)
            self.logger.debug(json.dumps(hjson, indent=4))
            return hjson
        except TimeoutError:
            self.logger.error("Time out!")
            return None

    # defined http post method
    def post(self, url, param):
        data = json.dumps(param)
        data = bytes(data, "utf-8")
        new_url = self.host + ":" + self.port + "/" + url
        self.logger.info('post data: \n' + json.dumps(param, indent=4))
        try:
            headers = {'Content-Type': 'application/json'}
            req = request.Request(new_url, data, headers)
            response = request.urlopen(req)
            res = response.read()
            hjson = json.loads(res)
            self.logger.debug(json.dumps(hjson, indent=4))
        except Exception as err:
            print(err, "\n")
        return hjson

# if __name__ == '__main__':
#     pass
