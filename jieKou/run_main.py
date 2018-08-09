# coding=utf-8
import unittest
import os
import time
from jieKou.common import HTMLTestRunner_cn


def all_case():
    '''
    加载指定目录下的所有用例
    # 待执行的目录
    '''
    basepath = os.path.realpath(os.path.dirname(__file__))
    print(basepath)
    casepath = os.path.join(basepath, "testcase/case")
    print(casepath)

    discovery = unittest.defaultTestLoader.discover(casepath, pattern="test*.py")
    print(discovery)
    now = time.strftime("%Y_%m_%d_%H_%M_%S")  # 时间戳
    reportpath = os.path.join(basepath, "report")
    print(reportpath)
    htmlpath = os.path.join(reportpath, "result%s.html" % now)
    print("report path:%s" %htmlpath)
    fp = open(htmlpath, "wb")
    runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp,
                                              title=u'自动化测试报告,测试结果如下：',
                                              description=u'用例执行情况：')

    # runner =HTMLTestRunner_cn.HTMLTestRunner(fp)   #简化版
    runner.run(discovery)
    fp.close()

    lists = os.listdir(reportpath)
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(reportpath, fn)))
    print(u'最新测试生成的报告： ' + lists[-1])
    # 找到最新生成的报告文件
    report_file = os.path.join(reportpath, lists[-1])
    print(report_file)


if __name__ == "__main__":
    all_case()

