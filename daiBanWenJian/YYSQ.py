#coding=utf-8
'''
    用印申请
    1.YYSQ(driver,toId)
'''
from buttomBtn import clickButtomBtn
from homePage import clickHomePage1Item
import clickListOne

pageName='YYSQ.py'

def YYSQ(driver,toId):
    print '点击首页--(%s)'%pageName
    clickButtomBtn(driver,'首页')
    print '点击待办文件--(%s)'%pageName
    clickHomePage1Item(driver, '待办文件')
    print '点击列表中第一条记录--(%s)'%pageName
    clickListOne(driver)
    temp=driver.find_element_by_id('com.cib.wbg:id/home_title_text').get_attribute('text')
    print temp
    if temp==u'用印申请':
        print '可以进行测试--(%s)'%pageName
        print '点击编辑--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/fab_expand_menu_button').click()
        print '点击文件办理--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_elements_by_id('com.cib.wbg:id/action_a')[0].click()
        print '填写意见--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/tv_yijian_item').send_keys('2017082501')
        print '下一处理步骤--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/tv_handler_value').click()
        print '选择下一处理步骤--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_elements_by_id('com.cib.wbg:id/check_file')[0].click()
        print '下一处理人--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/tv_handler_human_value').click()
        print '选择下一处理人--(%s)'%pageName
        print '点击搜索--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/add_mem_tag').click()
        print '输入员工号--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/add_mem_tag').send_keys(toId)
        print '隐藏键盘--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.hide_keyboard(); 
        print '选择搜索结果--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_class_name('android.widget.CheckBox').click()
        print '点击确定--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/btnOK').click()
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
    else:
        print '待更新...--(%s)'%pageName
        print '退回到首页--(%s)'%pageName
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()