import sys
sys.path.append('..')
sys.path.append('/youdaoledu2/StartEnd')
sys.path.append('/youdaoledu2/login')

from youdaoledu2.myunit import StartEnd
from youdaoledu2.login import Login_phone
from youdaoledu2.open_u3d import open_u3d
import unittest
import logging

class TestLogin(StartEnd):

    # def test_login_xrz12345(self):
    #     logging.info('=====testlogin_a12345=====')
    #     L = Login_phone(self.driver)
    #     L.login_pwd('15888509413', 'a12345')
    #
    #
    # def test_login_xrz888(self):
    #     L = Login_phone(self.driver)
    #     L.login_pwd('15888509413', '123456')
    #     # L.login_wrong()
    #
    # def test_login_error(self):
    #     L = Login_phone(self.driver)
    #     L.login_pwd('15888509412', 'a1234567')
    #     # L.login_wrong()

    def test_pwdlogin_openu3d(self):
        logging.info('=====testlogin_a12345=====')
        L = open_u3d(self.driver)
        L.openU3d()
        print('test pass')

if __name__ == '__main__':
    unittest.main()
