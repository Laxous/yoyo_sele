# coding=utf-8
import unittest
import time


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass初始化操作：用例开始前只执行一次")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass收尾操作：用例结束后只执行一次")

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

    def test_01(self):
        # time.sleep(1)
        print("执行用例01")
    def test_03(self):
        time.sleep(1)
        print("执行用例03")
    def test_02(self):
        time.sleep(1)
        print("执行用例02")
    def testadd(self):
        print("add")


if __name__ == "__main__":
    unittest.main()
