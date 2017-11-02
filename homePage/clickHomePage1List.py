#coding=utf-8
'''
    点击第一条记录并返回
'''

from tool.findElement import findElement

pageName='clickHomePage1List.py'

def clickHomePage1List(driver):
    driver.implicitly_wait(60)
    tempElement = findElement(driver, 'id', 'com.cib.wbg:id/list')
    element = findElement(tempElement, 'classes', 'android.widget.LinearLayout')
    element[0].click()
