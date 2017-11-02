#coding=utf-8
'''
    文件办理--日常事务审批
    1.handleRCSWSP(driver,toId1,toId2)
        toId1：下一处理人
        toId2：知悉人
'''

pageName='handleRCSWSP.py'

def handleRCSWSP(driver,toId1,toId2):
    print '填写意见--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/tv_yijian_item').send_keys('rcswsp01')
    
    print '点击下一处理步骤--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/tv_handler_value').click()
    print '选择下一处理步骤--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_elements_by_id('com.cib.wbg:id/check_file')[0].click()
    
    print '点击下一处理人--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/tv_handler_human_value').click()
    print '点击搜索--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/add_mem_tag').click()
    print '输入员工号--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/add_mem_tag').send_keys(toId1)
    print '点击确定--(%s)'%pageName+'--通过坐标确定，不同机子待更新'
    driver.implicitly_wait(10)
    driver.tap([(1010,1900)],500)
    print '选择搜索结果--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('android.widget.CheckBox').click()
    print '点击确定--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/mem_top_right_btn').click()
    
    print '点击知悉人--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/tv_titlezhixi').click()
    print '点击搜索--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/add_mem_tag').click()
    print '输入员工号--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/add_mem_tag').send_keys(toId2)
    print '点击确定--(%s)'%pageName+'--通过坐标确定，不同机子待更新'
    driver.implicitly_wait(10)
    driver.tap([(1010,1900)],500)
    print '选择搜索结果--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_class_name('android.widget.CheckBox').click()
    print '点击确定--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/mem_top_right_btn').click()
    
    print '点击交办--(%s)'%pageName
    driver.implicitly_wait(10)
    btn1=driver.find_element_by_id('com.cib.wbg:id/gv_chuli').find_elements_by_id('com.cib.wbg:id/query_btn')
    print btn1[1].get_attribute('text')
    if btn1[1].get_attribute('text')==u'交办':
        btn1[1].click()
    else:
        print '按钮错误--(%s)'%pageName

    print '确认交办--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/negativeButton').click()
    
    print '关闭成功提示框--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/negativeButton').click()
    
    print '退回到首页--(%s)'%pageName
    driver.implicitly_wait(10)
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
