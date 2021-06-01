# 楠哥
# 2021/5/31 23:58

def add(x,y):
    z=x+y
    return z
'''
print(add(3,4)==7)
print(add(3,4)==None)
print(add(1.2,4.5)==5.7)
'''

import  unittest

class  TestDemoAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("=============执行setupclass方法================")

    @classmethod
    def tearDownClass(cls) -> None:
        print("===============执行teardowncalss方法===================")

    def setUp(self) -> None:
        print("==========执行SetUp方法=========")

    def tearDown(self) -> None:
        print("=========执行teardown方法=======")

    def test_add01(self):
        print("=====执行test_001==========")
        self.assertEqual(7,add(3,4))

    def test_add02(self):
        print("=====执行test_002==========")
        self.assertEqual(None,add(3,4))

    def test_add03(self):
        print("=====执行test_003==========")
        self.assertEqual(5.7, add(1.2,4.5))

if __name__ == '__main__':
     unittest.main()