#coding=utf-8
'''
    日常事务审批，点击编辑子按钮
        1.clickModifyBtnRCSWSP(driver,modifyBtn,text)
            text：办结、流程意见、文件办理、会议意见
        2.需运行clickModifyBtn.py得到modifyBtn
'''

pageName='clickModifyBtnRCSWSP.py'

def clickModifyBtnRCSWSP(driver,modifyBtn,text):
    if text=='办结':
        print '点击%s--(%s)'%(text,pageName)
        modifyBtn[0].click()
    elif text=='流程意见':
        print '点击%s--(%s)'%(text,pageName)
        modifyBtn[1].click()
    elif text=='文件办理':
        print '点击%s--(%s)'%(text,pageName)
        modifyBtn[2].click()
    elif text=='会议意见':
        print '点击%s--(%s)'%(text,pageName)
        modifyBtn[3].click()
