#coding=utf-8
'''
    检查用印申请是否办理成功
    1.checkYYSQ(driver)
'''

from buttomBtn import clickButtomBtn
from homePage import clickHomePage1Item
import clickListOne

pageName='checkYYSQ.py'

def checkYYSQ(driver):
    print '点击首页--(%s)'%pageName
    clickButtomBtn(driver,'首页')
    print '点击待办文件--(%s)'%pageName
    clickHomePage1Item(driver, '待办文件')
    print '点击列表中第一条记录--(%s)'%pageName
    clickListOne(driver)
    temp=driver.find_element_by_id('com.cib.wbg:id/home_title_text').get_attribute('text')
    print temp
    if temp==u'用印申请':
        print '可以进行测试--(%s)'%pageName
        print '检查意见内容是否正确--(%s)'%pageName
        temp2=driver.find_element_by_id('com.cib.wbg:id/shangyi1').get_attribute('text')
        print temp2
        if temp2==u'2017082501':
            print '意见一致--(%s)'%pageName
            print '返回首页--(%s)'%pageName
            driver.implicitly_wait(10)
            driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
            driver.implicitly_wait(10)
            driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
        else:
            print '意见不一致，请检查处理是否成功--(%s)'%pageName
    else:
        print '待更新...--(%s)'%pageName