import unittest


class NumbersTest(unittest.TestCase):

    def test01(self):
        a = "北京-红歌"
        b = "honge"
        self.assertEqual(a, b, msg="失败原因：%s!= %s" % (a, b))

    def test02(self):
        '''判断 a in b '''
        a = "hello hongge"

        b = "hello hongge and world!"
        self.assertIn(a, b)

if __name__ == '__main__':
    unittest.main()