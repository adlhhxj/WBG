#coding=utf-8
'''
    点击正文、附件中的附件，以及查看更多
    1.clickAttachmentRCSWSP(driver)
'''
from initWBG.goBack import goBack
from time import sleep

pageName='clickAttachmentRCSWSP.py'

def clickAttachmentRCSWSP(driver):
    print '正文附件、附件的附件、查看更多--(%s)'%pageName
    flagZW=None
    try:
        btn1=driver.find_element_by_id('com.cib.wbg:id/text_word_attachment')
        flagZW=True
    except:
        print '正文没有附件--(%s)'%pageName
        flagZW=False
    if flagZW==True:
        print '正文有附件--(%s)'%pageName
        btn1.click()
        driver.implicitly_wait(10)
        goBack(driver, 'sys')
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_id('com.cib.wbg:id/text_word_attachment')
        except:
            print '返回失败，再次返回--(%s)'%pageName
            goBack(driver, 'sys')

    flagFJ=None
    try:
        btn2=driver.find_element_by_id('com.cib.wbg:id/text_word_attachment1')
        flagFJ=True
    except:
        print '附件中没有附件--(%s)'%pageName
        flagFJ=False    
    if flagFJ==True:
        print '附件中有附件--(%s)'%pageName
        driver.implicitly_wait(10)
        btn2.click()
        driver.implicitly_wait(10)
        try:
            driver.find_element_by_id('com.cib.wbg:id/text_word_attachment1')
        except:
            print '返回失败，再次返回--(%s)'%pageName
            goBack(driver, 'sys')
    
    print '向上滑动--(%s)'%pageName
    sleep(1)
    driver.swipe(500,1400,500,1000,1000)
    
    flagGD=None
    try:
        btn3=driver.find_element_by_id('com.cib.wbg:id/zuoxiangqing')
        flagGD=True
    except:
        flagGD=False
    if flagGD==True:
        print '点击查看更多--(%s)'%pageName
        btn3.click()
        goBack(driver, 'topleft')