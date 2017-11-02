#coding=utf-8
'''
    点击第一条记录
    1.clickListOne(driver)
'''

pageName='clickListOne.py'

def clickListOne(driver):
    print '点击第一条记录--(%s)'%pageName
    driver.implicitly_wait(10)
    try:
        btn=driver.find_element_by_id('com.cib.wbg:id/list').find_elements_by_class_name('android.widget.LinearLayout')
        btn[0].click()
    except:
        print '没有找到元素--(%s)'%pageName