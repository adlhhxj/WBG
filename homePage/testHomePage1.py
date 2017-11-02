#coding=utf-8
'''
    检查首页1个按钮，1行列表
'''

from clickHomePage1 import clickHomePage1
from checkHomePage1 import checkHomePage1
from shaiXuan import shaiXuan
from clickHomePage1List import clickHomePage1List
from tool.goBack import goBack


def testHomePage1(driver,text1,text2):
    clickHomePage1(driver, text1)
    checkHomePage1(driver, text1)
    shaiXuan(driver, text2)
    clickHomePage1List(driver)
    goBack(driver, 'topleft')
    goBack(driver, 'topleft')
    
    