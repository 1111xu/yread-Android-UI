from advance.baseView import BaseView
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By
from youdaoledu2.open import appium_desired



class First_start(BaseView):

    PrivacyLeftBtn = (By.ID,'com.youdao.yread:id/btnLeft')
    PrivacyRightBtn = (By.ID,'com.youdao.yread:id/btnRight')
    PopupCloseBtn = (By.ID,'com.youdao.yread:id/iv_popup_close')

    def check_PrivacyLeftBtn(self):
        logging.info("=============check_PrivacyLeftBtn============")
        try:
            element=self.driver.find_element(*self.PrivacyLeftBtn)
        except NoSuchElementException:
            logging.info('PrivacyLeftBtn element is not found!')
        else:
            logging.info('click PrivacyLeftBtn')
            element.click()

    def check_PrivacyRightBtn(self):
        logging.info("=============check_PrivacyRightBtn============")
        try:
            element=self.driver.find_element(*self.PrivacyRightBtn)
        except NoSuchElementException:
            logging.info('PrivacyRightBtn element is not found!')
        else:
            logging.info('click PrivacyRightBtn')
            element.click()

    def check_PopupCloseBtn(self):     #开机弹窗
        logging.info("=============check_PopupCloseBtn============")
        try:
            element=self.driver.find_element(*self.PopupCloseBtn)
        except NoSuchElementException:
            logging.info('PopupCloseBtn element is not found!')
        else:
            logging.info('click PopupCloseBtn')
            element.click()

if __name__ == '__main__':

    driver=appium_desired()
    com=First_start(driver)
    # com.check_PrivacyLeftBtn()
    com.check_PrivacyRightBtn()
    com.check_PopupCloseBtn()

