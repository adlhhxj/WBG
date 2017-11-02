#coding=utf-8

pageName='closeAppium.py'

def closeAppium(driver):
    print '关闭模拟器--(%s)'%pageName
    driver.implicitly_wait(5)
    driver.quit()