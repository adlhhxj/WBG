#coding=utf-8
'''
    点击编辑按钮，返回子按钮
    1.clickModifyBtn(driver)
    2.返回子按钮：return btn1
'''

pageName='clickModifyBtn.py'

def clickModifyBtn(driver):
    print '点击编辑按钮--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/fab_expand_menu_button').click()
    
    print '判断有几个按钮，及按钮功能--(%s)'%pageName
    btn1=driver.find_element_by_id('com.cib.wbg:id/multiple_actions').find_elements_by_class_name('android.widget.Button')
    btn1num=0
    for i in btn1:
        btn1num=btn1num+1
    print '按钮个数：%d--(%s)'%(btn1num,pageName)
    
    if btn1num==1:
        print '不能编辑--(%s)'%pageName
    else:
        print '返回子按钮，供后续使用--(%s)'%pageName
        return btn1