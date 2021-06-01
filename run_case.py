# 楠哥
# 2021/6/1 11:16
import unittest

#生成一个套件对象
suite = unittest.TestLoader().discover(start_dir='.',pattern="test*.py")

runner =unittest.TextTestRunner()
runner.run(suite)