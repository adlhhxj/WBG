#coding=utf-8
'''
    日常事务审批
'''
from clickAttachmentRCSWSP import clickAttachmentRCSWSP
from clickModifyBtn import clickModifyBtn
from clickModifyBtnRCSWSP import clickModifyBtnRCSWSP
from initWBG.goBack import goBack
from handleRCSWSP import handleRCSWSP
from initWBG.logoff import logoff
from initWBG.login import login
from checkRCSWSP import checkRCSWSP
from recoverRCSWSP import recoverRCSWSP

pageName='riChangShiWuShenPi.py'

def riChangShiWuShenPi(driver):
    print '日常事务审批--(%s)'%pageName
    title=driver.find_element_by_id('com.cib.wbg:id/home_title_text').get_attribute('text')
    print '标题：'+title.encode(encoding='UTF-8')+'--(%s)'%pageName
    
    clickAttachmentRCSWSP(driver) #点击正文附件、附件的附件、查看更多
    modifyBtn=clickModifyBtn(driver) #点击编辑按钮
    clickModifyBtnRCSWSP(driver, modifyBtn, '办结') #点击文件办理按钮
    goBack(driver, 'sys')
    clickModifyBtnRCSWSP(driver, modifyBtn, '流程意见') #点击文件办理按钮
    goBack(driver, 'sys')
    clickModifyBtnRCSWSP(driver, modifyBtn, '会议意见') #点击文件办理按钮
    goBack(driver, 'sys')
    clickModifyBtnRCSWSP(driver, modifyBtn, '文件办理') #点击文件办理按钮
    handleRCSWSP(driver, '011476', '011304') #第一个处理人，第二个知悉人
    
    logoff(driver) #退出帐号
    login(driver, '011476') #登录下一处理人帐号
    checkRCSWSP(driver) #检查是否收到该流程
    logoff(driver) #退出登录
    login(driver, '010073') #登录发起人帐号
    recoverRCSWSP(driver)
    
    
