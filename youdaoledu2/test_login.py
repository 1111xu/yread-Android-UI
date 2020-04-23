from youdaoledu2.myunit import StartEnd
from youdaoledu2.login import Login_phone
import unittest
import logging

class TestLogin(StartEnd):

    def test_login_xrz12345(self):
        logging.info('=====testlogin_a12345=====')
        L = Login_phone(self.driver)
        L.login_pwd('15888509413', 'a12345')


    def test_login_xrz888(self):
        L = Login_phone(self.driver)
        L.login_pwd('15888509413', '123456')
        # L.login_wrong()

    def test_login_error(self):
        L = Login_phone(self.driver)
        L.login_pwd('15888509412', 'a1234567')
        # L.login_wrong()


if __name__ == '__main__':
    unittest.main()
