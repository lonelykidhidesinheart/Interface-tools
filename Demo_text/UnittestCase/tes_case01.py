# coding = 'utf-8'
import requests
import unittest


class TestCase01(unittest.TestCase):
    # def setUp(self) -> None:
    #     self.a = 1
    #     print("case开始执行")
    #
    # def tearDown(self) -> None:
    #     print("case结束执行")

    @classmethod
    def setUpClass(cls) -> None:
        cls.a = 1
        print("case类开始执行")

    @classmethod
    def tearDownClass(cls) -> None:
        print("case类结束执行")

    def test_01(self):
        print(self.a)
        print("case01")
        pass

    def test_02(self):
        print(self.a)
        print("case02")
        pass

    def test_03(self):
        print(self.a)
        print("case03")
        pass


if __name__ == "__main__":
    unittest.main()
