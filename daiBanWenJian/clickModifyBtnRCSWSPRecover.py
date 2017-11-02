#coding=utf-8
'''
    回收日常事务审批，点击编辑子按钮
    1.clickModifyBtnRCSWSPRecover(driver,modifyBtn,text)
            text：办结、流程意见、文件办理、会议意见
    2.需运行clickModifyBtn.py得到modifyBtn
'''

pageName='clickModifyBtnRCSWSPRecover.py'

def clickModifyBtnRCSWSPRecover(driver,modifyBtn,text):
    if text=='文件办理':
        print '点击%s--(%s)'%(text,pageName)
        modifyBtn[0].click()
    elif text=='流程意见':
        print '点击%s--(%s)'%(text,pageName)
        modifyBtn[1].click()
    elif text=='会办意见':
        print '点击%s--(%s)'%(text,pageName)
        modifyBtn[2].click()