# coding=utf-8
import unittest
# help(unittest)  #查看帮助文档（unittest）
class IntegerArithmeticTestCase(unittest.TestCase):
    def testAdd(self):  # test method names begin with 'test'
        self.assertEqual((1 + 2), 4)
        self.assertEqual(0 + 1, 3)

    def testhehe(self):
        self.assertEqual(None, 1)
        self.assertEqual((5 * 8), 40)


if __name__ == '__main__':
    unittest.main()