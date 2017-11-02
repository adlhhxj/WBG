#coding=utf-8
'''
    返回上一页
    1.goBack(driver,text)
        text:系统返回 sys、页面左上角返回键 topleft
'''

pageName='goBack.py'

def goBack(driver,text):
    driver.implicitly_wait(60)
    if text=='sys':
        print '系统返回键--(%s)'%pageName
        driver.keyevent(4)
    if text=='topleft':
        print '左上角返回按钮--(%s)'%pageName
        driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()