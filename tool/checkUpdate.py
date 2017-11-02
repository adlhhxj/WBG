#coding=utf-8

pageName='checkUpdate.py'

def checkUpdate(driver):
    print '检查是否有更新说明提示框--(%s)'%pageName
    flag=None
    try:
        driver.find_element_by_id('com.cib.wbg:id/img_close')
        flag=True
    except:
        flag=False
    
    if flag==True:
        print '有更新说明提示框，点击小叉叉退出更新--(%s)'%pageName
        driver.implicitly_wait(5)
        driver.find_element_by_id('com.cib.wbg:id/img_close').click()
    else:
        print '没有更新说明提示框--(%s)'%pageName