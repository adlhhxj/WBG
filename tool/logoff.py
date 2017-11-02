#coding=utf-8
'''
    退出帐号，退出后检查是否有升级提示框
    1.logoff(driver)
    2.点击我的--点击设置--点击退出登录
'''
from tool.checkUpdate import checkUpdate

pageName='logoff.py'

def logoff(driver):
    print '退出帐号--(%s)'%pageName
    print '点击我的--(%s)'%pageName
    driver.implicitly_wait(3)
    driver.find_element_by_id('com.cib.wbg:id/mine_btn_text').click()
    print '点击设置--(%s)'%pageName
    driver.implicitly_wait(3)
    driver.find_element_by_id('com.cib.wbg:id/settings_layout').click()
    print '点击退出登录--(%s)'%pageName
    driver.implicitly_wait(3)
    driver.find_element_by_id('com.cib.wbg:id/exit_login').click()
    print '点击确定--(%s)'%pageName
    driver.implicitly_wait(3)
    driver.find_element_by_id('android:id/button1').click()

    print '检查退出帐号后是否会弹出更新页面--(%s)'%pageName
    driver.implicitly_wait(3)
    checkUpdate(driver)
