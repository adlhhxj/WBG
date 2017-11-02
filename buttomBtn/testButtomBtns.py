#coding=utf-8
'''
    测试底部5个按钮
    1.testButtomBtns(driver,text)
'''

from testButtomBtn import testButtomBtn

pageName='testButtomBtns.py'

def testButtomBtns(driver):
    testButtomBtn(driver,'我的')
    testButtomBtn(driver,'工作圈')
    testButtomBtn(driver,'通讯录')
    testButtomBtn(driver,'微聊')
    testButtomBtn(driver,'首页')