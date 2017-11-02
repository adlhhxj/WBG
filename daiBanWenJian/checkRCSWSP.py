#coding=utf-8
'''
    检查日常事务审批是否办理成功，然后返回首页
    1.checkRCSWSP(driver)
'''
from buttomBtn.clickButtomBtn import clickButtomBtn
from homePage.clickHomePage1Item import clickHomePage1Item
from clickListOne import clickListOne
from shaiXuan import shaiXuan

pageName='checkRCSWSP.py'

def checkRCSWSP(driver):
    print '点击首页--(%s)'%pageName
    clickButtomBtn(driver,'首页')
    print '点击待办文件--(%s)'%pageName
    clickHomePage1Item(driver, '待办文件')
    print '筛选--(%s)'%pageName
    shaiXuan(driver, '日常事务审批')
    print '点击第一条记录--(%s)'%pageName
    clickListOne(driver)
    
    print '检查意见内容是否正确--(%s)'%pageName
    temp2=driver.find_element_by_id('com.cib.wbg:id/shangyi1').get_attribute('text')
    print '上一意见：'+temp2.encode(encoding='UTF-8')
    if temp2==u'rcswsp01':
        print '意见一致--(%s)'%pageName
        print '返回首页--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
