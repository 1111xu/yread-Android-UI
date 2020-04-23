from  appium import  webdriver
import logging
import yaml
import logging.config
from os import path


# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s')

url='root_path_of_project/'


log_file_path = path.join(path.dirname(path.abspath(__file__)), 'cap/log.conf') #需要绝对路径
logging.config.fileConfig(log_file_path)
logging=logging.getLogger()

log_desired_path = path.join(path.dirname(path.abspath(__file__)), 'cap/desired_caps') #需要绝对路径
file = open(log_desired_path, 'r')
data=yaml.load(file)

def appium_desired():

    log_desired_path = path.join(path.dirname(path.abspath(__file__)), 'cap/desired_caps') #需要绝对路径
    file = open(log_desired_path, 'r')
    data=yaml.load(file)

    desired_caps={}
    desired_caps['platformName']=data['platformName']
    desired_caps['platformVersion']=data['platformVersion']
    desired_caps['deviceName']=data['deviceName']

    desired_caps['unicodeKeyboard']=True
    desired_caps['resetKeyboard']=True
    desired_caps['automationName']='uiautomator2'

    #desired_caps['app']=data['app']
    desired_caps['appPackage']=data['appPackage']
    desired_caps['appActivity']=data['appActivity']

    desired_caps['noReset']=data['noReset']

    logging.info('打开app')
    driver=webdriver.Remote('http://'+str(data['ip'])+':'+str(data['port'])+'/wd/hub',desired_caps)

    driver.implicitly_wait(8)
    return driver

if __name__=='__main__':
    appium_desired()