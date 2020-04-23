# coding=utf-8


import logging
from youdaoledu2.open import appium_desired,webdriver
from youdaoledu2.First_start import First_start
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import TimeoutException
from time import sleep



class Login_phone(First_start):

    PhoneNumber=(By.ID,'com.youdao.yread:id/etPhoneNumber')
    userPwd=(By.ID,'com.youdao.yread:id/etPassword')
    loginBtn=(By.ID,'com.youdao.yread:id/btnLogin')

    def login_pwd(self,phoneNumber,userpwd):

        self.check_PrivacyRightBtn()
        self.check_PopupCloseBtn()

        logging.info('==========into_loginpage=========')
        self.driver.find_element(By.ID, 'com.youdao.yread:id/ivAvatar').click()

        self.driver.find_element(By.ID,'com.youdao.yread:id/btnLoginByPhone').click()  # 进入手机登录
        logging.info('==========into_pwdlogin=========')
        self.driver.find_element(By.ID,"com.youdao.yread:id/tvLoginByPassword").click()

        logging.info('==========pwdlogin=========')
        logging.info('input username:%s'%phoneNumber)
        self.driver.find_element(*self.PhoneNumber).send_keys(phoneNumber)

        logging.info('input userpwd:%s'%userpwd)
        self.driver.find_element(*self.userPwd).send_keys(userpwd)

        logging.info('click loginBtn')
        self.driver.find_element(*self.loginBtn).click()

    def get_toast(driver, text=None, timeout=5, poll_frequency=0.5):
        """
        get toast
        :param driver: driver
        :param text: toast text
        :param timeout: Number of seconds before timing out, By default, it is 5 second.
        :param poll_frequency: sleep interval between calls, By default, it is 0.5 second.
        :return: toast
        """
        if text:
            toast_loc = ("//*[contains(@text, '%s')]" % text)
        else:
            toast_loc = "//*[@class='android.widget.Toast']"

        try:
            WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(('xpath', toast_loc)))
            toast_elm = driver.find_element_by_xpath(toast_loc)
            return toast_elm

        except:
            return "Toast not found"

    # def login_wrong(self):
    #     try:
    #         vendortext = "账号或密码错误"
    #         toast_element = '//*[@text=\'{}\']'.format(vendortext)
    #         toast = WebDriverWait(driver, 1).until(lambda driver: driver.find_element(By.XPATH,toast_element))
    #
    #     # toast=WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH,toast_element)))
    #     except TimeoutException:
    #         logging.info('Time Out!,Toast not found')
    #     else:
    #         print(toast.text)

        logging.info('login failed')


if __name__ == '__main__':

    driver=appium_desired()
    L=Login_phone(driver)
    L.login_pwd('15888509413','abc12345')





