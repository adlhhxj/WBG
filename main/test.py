#coding=utf-8
'''
    调试功能
'''
from tool.setup import setup
from tool.logon import logon
from tool.closeAppium import closeAppium
from time import sleep
from homePage.testHomePage1 import testHomePage1

pageName='mainWBG.py'

#初始化
driver=setup()

#登录
logon(driver)

#首页点击菜单测试
testHomePage1(driver, '待办文件', '通知')







'''
sleep(3)
closeAppium(driver) #关闭模拟器
'''
