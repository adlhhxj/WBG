#coding=utf-8
'''
    撤回用印申请
    1.recoverYYSQ(driver)
'''
from buttomBtn import clickButtomBtn
from homePage import clickHomePage1Item
import clickListOne

pageName='recoverYYSQ.py'

def recoverYYSQ(driver):
    print '撤回用印申请--(%s)'%pageName
    clickButtomBtn(driver,'首页')
    print '点击已办文件--(%s)'%pageName
    clickHomePage1Item(driver, '已办文件')
    print '点击列表中第一条记录--(%s)'%pageName
    clickListOne(driver)

    print '点击编辑--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/fab_expand_menu_button').click()
    print '点击文件办理--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_elements_by_id('com.cib.wbg:id/action_a')[0].click()
    print '填写收回原因--(%s)'%pageName
    driver.find_element_by_id('com.cib.wbg:id/btnRevok').click()
    driver.find_element_by_id('com.cib.wbg:id/btnRevok').send_keys('test')
    print '点击清除上一意见--(%s)'%pageName
    driver.find_element_by_id('com.cib.wbg:id/cb_clear').click()
    
    print '点击收回--(%s)'%pageName
    driver.find_element_by_id('com.cib.wbg:id/btnRevok').click()
    print '点击确定--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/negativeButton').click()
    print '退回到首页--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
