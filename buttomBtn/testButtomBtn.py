#coding=utf-8
'''
    测试底部5个按钮中的一个
    1.testButtomBtn(driver,text)
'''

from clickButtomBtn import clickButtomBtn
from checkButtomBtn import checkButtomBtn

pageName='testButtomBtn.py'

def testButtomBtn(driver,text):
    clickButtomBtn(driver,text)
    checkButtomBtn(driver,text)
