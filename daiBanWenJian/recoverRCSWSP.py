#coding=utf-8
'''
    撤回日常事务审批
    1.recoverRCSWSP(driver)
'''
from buttomBtn.clickButtomBtn import clickButtomBtn
from homePage.clickHomePage1Item import clickHomePage1Item
from clickListOne import clickListOne
from shaiXuan import shaiXuan
from clickModifyBtn import clickModifyBtn
from clickModifyBtnRCSWSPRecover import clickModifyBtnRCSWSPRecover

pageName='recoverRCSWSP.py'

def recoverRCSWSP(driver):
    print '点击首页--(%s)'%pageName
    clickButtomBtn(driver,'首页')
    print '点击已办文件--(%s)'%pageName
    clickHomePage1Item(driver, '已办文件')
    print '筛选--(%s)'%pageName
    shaiXuan(driver, '日常事务审批')
    print '点击第一条记录--(%s)'%pageName
    clickListOne(driver)
    
    print '点击编辑按钮--(%s)'%pageName
    modifyBtn=clickModifyBtn(driver)
    print '点击文件办理--(%s)'%pageName
    clickModifyBtnRCSWSPRecover(driver, modifyBtn, '文件办理')

    print '填写收回原因--(%s)'%pageName
    driver.find_element_by_id('com.cib.wbg:id/btnRevok').click()
    driver.find_element_by_id('com.cib.wbg:id/btnRevok').send_keys('test')
    print '隐藏键盘--(%s)'%pageName
    driver.implicitly_wait(3)
    driver.hide_keyboard()
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
