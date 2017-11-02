#coding=utf-8
'''
    初始化driver模拟器
'''

from appium import webdriver
import exitCode

pageName='setup.py'

def setup():
    print '初始化driver模拟器--(%s)'%pageName
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = 'Android Emulator'
    desired_caps['appPackage'] = 'com.cib.wbg'
    desired_caps['appActivity'] = 'com.cib.xyh.activity.home.StartPageActivity'
    desired_caps["unicodeKeyboard"] = "True"
    desired_caps["resetKeyboard"] = "True"
    print '正在打开软件，耗时比较长，请稍候...--(%s)'%pageName
    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        return driver
    except:
        print '模拟器打开失败，请重新开启appium--(%s)'%pageName
        exitCode()