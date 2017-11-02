#coding=utf-8
'''
    获取屏幕分辨率
    1.getScreenSize(driver,text)
    2.text=width：宽度
    3.text=height：高度
'''

pageName='getScreenSize.py'

def getScreenSize(driver,text):
    print '获取屏幕分辨率--(%s)'%pageName
    if text=='width':
        return driver.get_window_size()['width']
    if text=='height':
        return driver.get_window_size()['height']