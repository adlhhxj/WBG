#coding=utf-8
from time import sleep

pageName='clickPeiZhi.py'

def clickPeiZhi(driver):
    print '点击配置'
    driver.find_element_by_id('com.cib.wbg:id/display_setting_layout').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    print '返回我的'
    sleep(1)
    driver.keyevent(4)