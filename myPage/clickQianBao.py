#coding=utf-8
from time import sleep

pageName='clickPeiZhi.py'

def clickQianBao(driver):
    print '点击钱包'
    driver.find_element_by_id('com.cib.wbg:id/my_wallet_layout').click()
    print '点击财富总览-详情-ui中点击不到...'
    
    print '点击视频会议'
    driver.find_element_by_id('com.cib.wbg:id/ll_polycom').click()
    print '点击通讯录'
    driver.find_element_by_id('com.cib.wbg:id/left_button').click()
    print '点击预约会议'
    driver.find_element_by_id('com.cib.wbg:id/yy_poly_button').click()
    print '点击拨号'
    driver.find_element_by_id('com.cib.wbg:id/right_button').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    
    print '点击会议签到'
    driver.find_element_by_id('com.cib.wbg:id/ll_signin_layout').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    
    print '点击红包记录'
    driver.find_element_by_id('com.cib.wbg:id/ll_redpacked_layout').click()
    print '系统返回，返回钱包'
    sleep(1)
    driver.keyevent(4)
    
    print '点击生活商城'
    driver.find_element_by_id('com.cib.wbg:id/ll_life_store').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    print '钱包页面'
    sleep(1)
    driver.keyevent(4)
    
    print '点击钱大掌柜'
    driver.find_element_by_id('com.cib.wbg:id/ll_qianda').click()
    print '系统返回，返回钱包'
    sleep(1)
    driver.keyevent(4)
    
    print '点击智能投顾'
    driver.find_element_by_id('com.cib.wbg:id/wisdom_invest_layout').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    
    print '点击信用卡'
    driver.find_element_by_id('com.cib.wbg:id/ll_credit_card_layout').click()
    print '点击信用卡申请'
    driver.find_element_by_id('com.cib.wbg:id/ll_creditcard_apply').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    print '点击分期付款申请'
    driver.find_element_by_id('com.cib.wbg:id/ll_installment_payment').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    print '点击兴乐购'
    driver.find_element_by_id('com.cib.wbg:id/ll_shop_apply').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    print '点击我的信用卡'
    driver.find_element_by_id('com.cib.wbg:id/ll_creditcard_info').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    print '点击申请记录查询'
    driver.find_element_by_id('com.cib.wbg:id/ll_apply_recode').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    print '系统返回，返回钱包页面'
    sleep(1)
    driver.keyevent(4)
    
    print '向上滑动，显示出证券开户菜单'
    sleep(1)
    driver.swipe(500,1300,500,900,500)
    sleep(1)

    print '点击消费贷款'
    driver.find_element_by_id('com.cib.wbg:id/ll_consume_loan').click()
    print '系统返回'
    sleep(2)
    driver.keyevent(4)
    sleep(2)
    
    print '点击员工贷款'
    driver.find_element_by_id('com.cib.wbg:id/loans_layout').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    
    print '点击热销产品'
    driver.find_element_by_id('com.cib.wbg:id/trust_layout').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    
    print '点击证券开户，测试环境页面加载不出来，会白屏，系统返回键没响应。先关闭此项测试'
#    driver.find_element_by_id('com.cib.wbg:id/ll_huafu_sdk').click()
#    driver.implicitly_wait(5)
#    print '点击屏幕返回'
#    driver.tap([(50,50)],500)
