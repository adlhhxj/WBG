#coding=utf-8
from time import sleep

pageName='clickSheZhi.py'

def clickSheZhi(driver):
    print '点击设置'
    driver.find_element_by_id('com.cib.wbg:id/settings_layout').click()
    print '点击功能设置'
    driver.find_element_by_id('com.cib.wbg:id/txv_functionsetting').click()
    print '点击是否添加常用联系人'
    driver.find_element_by_id('com.cib.wbg:id/btn_constact').click()
    print '再次点击是否添加常用联系人'
    driver.find_element_by_id('com.cib.wbg:id/btn_constact').click()
    print '点击是否开启快速交办'
    driver.find_element_by_id('com.cib.wbg:id/btn_quick_jiaoban').click()
    print '再次点击是否开启快速交办'
    driver.find_element_by_id('com.cib.wbg:id/btn_quick_jiaoban').click()
    print '点击选择登录方式'
    driver.find_element_by_id('com.cib.wbg:id/login_mode').click()
    print '点击手势滑动登录'
    driver.find_element_by_id('com.cib.wbg:id/gesture_login').click()
    print '点击取消'
    driver.find_element_by_name('取消').click()
    print '再次点击手势滑动登录'
    driver.find_element_by_id('com.cib.wbg:id/gesture_login').click()
    print '点击确定'
    driver.find_element_by_name('确定').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    
    print '再次点击选择登录方式'
    driver.find_element_by_id('com.cib.wbg:id/login_mode').click()
    print '点击传统登录'
    driver.find_element_by_id('com.cib.wbg:id/tradition_login').click()
    print '点击取消'
    driver.find_element_by_name('取消').click()
    print '再次点击传统登录'
    driver.find_element_by_id('com.cib.wbg:id/tradition_login').click()
    print '点击确定'
    driver.find_element_by_name('确定').click()

    print '点击文件打开方式'
    driver.find_element_by_id('com.cib.wbg:id/openfile').click()
    print '点击WPS Office'
    driver.find_element_by_id('com.cib.wbg:id/wps_btn').click()
    print '再次点击WPS Office'
    driver.find_element_by_id('com.cib.wbg:id/wps_btn').click()
    print '点击返回'
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
    
    print '返回设置'
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
    print '点击微聊设置'
    driver.find_element_by_id('com.cib.wbg:id/txv_chatsetting').click()
    print '点击消息设置'
    driver.find_element_by_id('com.cib.wbg:id/message_setting').click()
    print '点击声音'
    driver.find_element_by_id('com.cib.wbg:id/voice_btn').click()
    print '再次点击声音'
    driver.find_element_by_id('com.cib.wbg:id/voice_btn').click()
    print '点击震动'
    driver.find_element_by_id('com.cib.wbg:id/shake_btn').click()
    print '再次点击震动'
    driver.find_element_by_id('com.cib.wbg:id/shake_btn').click()
    print '点击消息预览'
    driver.find_element_by_id('com.cib.wbg:id/message_preview_btn').click()
    print '再次点击消息预览'
    driver.find_element_by_id('com.cib.wbg:id/message_preview_btn').click()
    print '点击听筒模式'
    driver.find_element_by_id('com.cib.wbg:id/receiver_mode_btn').click()
    print '再次点击听筒模式'
    driver.find_element_by_id('com.cib.wbg:id/receiver_mode_btn').click()
    print '点击免打扰'
    driver.find_element_by_id('com.cib.wbg:id/no_disturb_btn').click()
    print '点击免打扰按钮'
    driver.find_element_by_id('com.cib.wbg:id/no_disturbing_btn').click()
    print '再次点击免打扰按钮'
    driver.find_element_by_id('com.cib.wbg:id/no_disturbing_btn').click()
    print '点击返回'
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
    print '返回微聊设置'
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
    
    print '点击安全与隐私'
    driver.find_element_by_id('com.cib.wbg:id/safety_privacy').click()
    print '点击多处登录管理'
    driver.find_element_by_id('com.cib.wbg:id/landing_manage_btn').click()
    print '点击返回'
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
    print '点击黑名单'
    driver.find_element_by_id('com.cib.wbg:id/blacklist_btn').click()
    print '点击返回'
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
    print '返回微聊设置'
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
    
    print '点击清空聊天记录'
    driver.find_element_by_id('com.cib.wbg:id/clear_message_history').click()
    print '点击取消'
    driver.find_element_by_id('com.cib.wbg:id/clear_cancel').click()
    print '点击返回'
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
    
    print '点击关于'
    driver.find_element_by_id('com.cib.wbg:id/about').click()
    print '点击检查更新'
    driver.find_element_by_id('com.cib.wbg:id/update').click()
    print '点击意见和反馈'
    driver.find_element_by_id('com.cib.wbg:id/suggestion').click()
    print '填写意见待更新...'
    print '点击提交'
    driver.find_element_by_id('com.cib.wbg:id/btn_commit').click()
    print '点击返回'
    driver.find_element_by_id('com.cib.wbg:id/top_left_btn').click()
    print '点击帮助'
    driver.find_element_by_id('com.cib.wbg:id/help').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    print '点击分享'
    driver.find_element_by_id('com.cib.wbg:id/share').click()
    print '系统返回'
    sleep(1)
    driver.keyevent(4)
    print '系统返回，返回我的页面'
    sleep(1)
    driver.keyevent(4)