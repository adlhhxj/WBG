#coding=utf-8
from tool.closeAppium import closeAppium
from tool.exitCode import exitCode

pageName='checkNet.py'

def checkNet(driver):
    print '检查是否在内网--(%s)'%pageName
    try:
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/login')
    except:
        print 'error：网络异常--(%s)'%pageName
        closeAppium(driver)
        exitCode()

