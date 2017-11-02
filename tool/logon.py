#coding=utf-8
'''
    登录
    1.logon(driver,idNo)
'''
from tool.closeAppium import closeAppium
from tool.exitCode import exitCode
from imgLocation.inputPwd import inputPwd
from config.getConfig import getConfig
from tool.findElement import findElement
from checkUpdate import checkUpdate
from checkNet import checkNet

pageName='logon.py'

def logon(driver):
    print '登录--(%s)'%pageName
#检查更新提示框
    checkUpdate(driver)
    
#检查网络
    checkNet(driver)

#清空账号
    element = findElement(driver, 'id', 'com.cib.wbg:id/imgcancle')
    element.click()

#输入账号
    logonID = getConfig('setup', 'logonID')
    driver.find_element_by_id('com.cib.wbg:id/username').send_keys(logonID)

#输入密码
    pwd=getConfig('setup', 'logonPwd')  #从配置文件中读取密码
    inputPwd(driver, pwd)

#点击登录按钮
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/login').click()

    try:
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/home_btn')
    except:
        print '登录失败--(%s)'%pageName
        closeAppium(driver)
        exitCode()