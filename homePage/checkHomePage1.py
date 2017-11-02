#coding=utf-8
'''
    检查跳转是否正确
'''

from tool.findElement import findElement

pageName='checkHomePage1.py'

def checkHomePage1(driver,text):
    driver.implicitly_wait(60)
    Element = findElement(driver, 'id', 'com.cib.wbg:id/home_title_text')
    ElementText = Element.get_attribute('text')
    if ElementText == unicode(text,'utf-8'):
        print '%s 刷新正确 %s'%(text,pageName)
    else:
        print '%s 刷新错误 %s'%(text,pageName)
