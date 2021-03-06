import unittest
from youdaoledu2.open import appium_desired
import logging
from time import sleep
import warnings

class StartEnd(unittest.TestCase):

    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        logging.info('=========setUp========')
        self.driver=appium_desired()

    def tearDown(self):
        logging.info('=========tearDown========')
        sleep(5)
        self.driver.close_app()

