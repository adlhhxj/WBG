#coding=utf-8
'''
    筛选待办文件类型
    1.shaiXuan(driver,text)
        text:部门会办、通知、通知转办、授权设置、发文、收文、会议安排、部门阅办、
                    呈批(阅)件、用印申请、日常事务审批、维护受理、舆情监测报告、每日金融与每日经济、
                    行领导重要活动安排、利率申请审批
'''

from tool.findElement import findElement

pageName='shaiXuan.py'

def shaiXuan(driver,text):
    #点击筛选
    elementSX = findElement(driver, 'id', 'com.cib.wbg:id/llopinion')
    elementSX.click()
    #点击筛选内容
    elementSXC = findElement(driver, 'name', text)
    elementSXC.click()
    #点击确定
    elementSXQ = findElement(driver, 'id', 'com.cib.wbg:id/btnOk')
    elementSXQ.click()
