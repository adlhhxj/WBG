#coding=utf-8

from clickHomePage1Item import clickHomePage1Item
from homePage import clickHomePage1List
from homePage import checkHomePage1
from clickHomePage2Item import clickHomePage2Item

pageName='allHomePageTest.py'

def allHomePageTest(driver):
    clickHomePage1Item(driver,'待办文件')
    clclickHomePage1Oneriver)
    checkHomePage1(driver, '待办文件')
    clickHomePage1Item(driver,'待阅文件')
    clickHclickHomePage1Oner)
    checkHomePage1(driver, '待阅文件')
    clickHomePage1Item(driver,'已办文件')
    clickHomePclickHomePage1One    checkHomePage1(driver, '已办文件')
    clickHomePage1Item(driver,'已阅文件')
    clickHomePage1clickHomePage1OnecheckHomePage1(driver, '已阅文件')
    clickHomePage1Item(driver,'会议安排')
    clickHomePage1ListclickHomePage1OnekHomePage1(driver, '会议安排')
    clickHomePage1Item(driver,'日程管理')
    checkHomePage1(driver, '日程管理')
    clickHomePage1Item(driver,'授权管理')
    checkHomePage1(driver, '授权管理')
    clickHomePage1Item(driver,'电子邮件')
    checkHomePage1(driver, '电子邮件')

    clickHomePage2Item(driver)