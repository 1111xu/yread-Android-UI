# coding=utf-8


# Windows下cmd运行python脚本报错“ModuleNotFoundError 或者 ImportError： No Module named ...”的解决方法
import sys
sys.path.append('..')
sys.path.append('/youdaoledu2/open')
sys.path.append('/youdaoledu2/login')


import logging
from youdaoledu2.open import *
from youdaoledu2.login import *
from selenium.webdriver.common.by import By
from time import sleep
import yaml
from os import path



from selenium.webdriver.support.ui import WebDriverWait

log_desired_path = path.join(path.dirname(path.abspath(__file__)), 'cap/desired_caps')  # 需要绝对路径
file = open(log_desired_path, 'r')
data = yaml.load(file)
desired_caps={}
desired_caps['noReset'] = data['noReset']

class open_u3d(Login_phone):


    def open_course(self):

        logging.info('==========into_coursepage=========')
        self.driver.find_element(By.ID, "com.youdao.yread:id/ivTabCourse").click()
        logging.info('==========open u3dcourse=========')
        self.driver.find_element(By.XPATH, "//android.widget.TextView[@text='动物宝宝']").click()

    def getPermit(self):

        if desired_caps['noReset']==False:

            L.login_pwd('15888509413', 'abc12345')
            sleep(5)
            self.check_PopupCloseBtn()
            self.open_course()
            logging.info('==========get_permission=========')
            self.driver.find_element(By.ID, "com.youdao.yread:id/btnStart").click()

            #针对魅族MX6手机，连点三次允许，可优化成：直到未找到btn时，不再点击
            self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
            self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()
            self.driver.find_element(By.ID, "com.android.packageinstaller:id/permission_allow_button").click()

            # self.driver.find_element(By.ID, "com.youdao.yread:id/btnStart").click()
            # self.driver.find_element(By.ID, "com.youdao.yread:id/btnStart").click()
            logging.info('==========start_study=========')
            self.driver.find_element(By.ID, "com.youdao.yread:id/btnStart").click()
        else:
            self.open_course()
            print(desired_caps['noReset'])


if __name__ == '__main__':
    driver = appium_desired()
    L = open_u3d(driver)
    L.getPermit()
