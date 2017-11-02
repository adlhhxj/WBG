#coding=utf-8
from time import sleep

pageName='clickHomePage2Item.py'

def clickHomePage2Item(driver):
    print '滑动到第二页--(%s)'%pageName
    sleep(2)
    driver.swipe(750,480,250,480,500)
    sleep(2)
    try:
        btn2=driver.find_element_by_id('com.cib.wbg:id/gridview').find_elements_by_class_name('android.widget.RelativeLayout')
    except:
        print '找不到元素--(%s)'%pageName
    temp=0
    for i in btn2:
        temp=temp+1
    print '总共有%s个菜单--(%s)'%(temp,pageName)
    
    
    print '滑动到第一页--(%s)'%pageName
    sleep(2)
    driver.swipe(250,480,750,480,500)
    sleep(2)
