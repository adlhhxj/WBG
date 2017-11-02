#coding=utf-8
from time import sleep

pageName='clickShouCan.py'

def clickShouCan(driver):
    print '点击收藏'
    driver.find_element_by_id('com.cib.wbg:id/my_collect_layout').click()
    print '系统返回，返回我的'
    sleep(1)
    driver.keyevent(4)