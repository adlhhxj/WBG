#coding=utf-8
'''
    用印申请
    1.yongYinShenQing(driver)
'''

from YYSQ import YYSQ
from checkYYSQ import checkYYSQ
from recoverYYSQ import recoverYYSQ
from initWBG.logoff import logoff
from initWBG.logon import logon

pageName='yongYinShenQing.py'

def yongYinShenQing(driver):
    print '用印申请--(%s)'%pageName
    title=driver.find_element_by_id('com.cib.wbg:id/home_title_text').get_attribute('text')
    print '标题：'+title.encode(encoding='UTF-8')+'--(%s)'%pageName
    
    
    YYSQ(driver,'011476')
    logoff(driver)
    login(driver,'011476')
    checkYYSQ(driver)
    logoff(driver)
    login(driver,'011304')
    recoverYYSQ(driver)