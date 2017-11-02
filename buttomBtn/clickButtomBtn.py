#coding=utf8
'''
    点击底部5个按钮
    1.clickButtomBtn(driver,text)
'''

pageName='clickButtomBtn.py'

def clickButtomBtn(driver,text):
    print '点击%s--(%s)'%(text,pageName)
    try:
        if text=='我的':
            driver.find_element_by_id('com.cib.wbg:id/mine_btn').click()
        elif text=='工作圈':
            driver.find_element_by_id('com.cib.wbg:id/work_circel_btn').click()
        elif text=='通讯录':
            driver.find_element_by_id('com.cib.wbg:id/address_book_btn').click()
        elif text=='微聊':
            driver.find_element_by_id('com.cib.wbg:id/message_btn').click()
        elif text=='首页':
            driver.find_element_by_id('com.cib.wbg:id/home_btn').click()   
    except:
        print '找不到元素 %s--(%s)'%(text,pageName)

