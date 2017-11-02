#coding=utf8
'''
    检查页面跳转
    1.checkButtomBtn(driver,text)
'''

pageName='checkButtomBtn.py'

def checkButtomBtn(driver,text):
    driver.implicitly_wait(10)
    try:
        if text=='我的':
            driver.find_element_by_id('com.cib.wbg:id/mine_headpic_img')
        elif text=='工作圈':
            driver.find_element_by_id('com.cib.wbg:id/workgroup_bg')
        elif text=='通讯录':
            driver.find_element_by_id('com.cib.wbg:id/address_search_edit')
        elif text=='微聊':
            driver.find_element_by_id('com.cib.wbg:id/message_search_btn')
        elif text=='首页':
            driver.find_element_by_id('com.cib.wbg:id/imgDaiBan')
        print '页面刷新正常 %s--(%s)'%(text,pageName)
    except:
        print '页面刷新失败 %s--(%s)'%(text,pageName)