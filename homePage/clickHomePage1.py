#coding=utf-8
'''
    点击首页菜单
'''

from tool.findElement import findElement

pageName='clickHomePage1.py'

def clickHomePage1(driver,text):
    tempElement = findElement(driver, 'id', 'com.cib.wbg:id/gridview')
    element = findElement(tempElement, 'classes', 'android.widget.LinearLayout')

    if text=='待办文件':
        element[0].click()
    elif text=='待阅文件':
        element[1].click()
    elif text=='已办文件':
        element[2].click()
    elif text=='已阅文件':
        element[3].click()
    elif text=='会议安排':
        element[4].click()
    elif text=='日程管理':
        element[5].click()
    elif text=='授权管理':
        element[6].click()
    elif text=='电子邮件':
        element[7].click()




