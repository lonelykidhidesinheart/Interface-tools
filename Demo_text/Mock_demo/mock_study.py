# coding=utf-8
from unittest import mock
import unittest
import requests


# def post_request(url, data):
#     res = requests.post(url, data).json()
#     print(res)
#     return res


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print('case执行结束')

    def test_01(self):
        url = "http://127.0.0.1:5000/post/user/login"
        data = {
            "username": 2,
        }
        sucess_test = mock.Mock(return_value=data)
        post_request = sucess_test
        res = post_request

        self.assertEqual(1, res()['username'], msg="失败原因：%s!= %s" % ('1', res()['username']))


if __name__ == "__main__":
    # 创建TstSuite对象
    suite = unittest.TestSuite()

    # # 声明一个TestCase 列表，列表中的TestCase顺序，代表测试用例的执行顺序
    # tests = [TestLogin("test_add")]
    #
    # # 将TestCase放入TsetSuit中
    # suite.addTests(tests)

    # 直接用addTest方法添加单个TestCase
    suite.addTest(TestLogin("test_01"))

    # 创建TextTestRunner对象(用来运行TestSuit)
    runner = unittest.TextTestRunner(verbosity=2)  # verbosity代表信息显示的详细程度，分为 0,1,2 ，0最简单、2最详细
    # 执行TestSuite
    runner.run(suite)
