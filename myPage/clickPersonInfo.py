#coding=utf-8
from time import sleep

pageName='clickPersonInfo.py'

def clickPersonInfo(driver):
    print '获取姓名'
    name=driver.find_element_by_id('com.cib.wbg:id/mine_name_text').get_attribute('text')
    
    print name
    
    print '点击个人信息'
    driver.find_element_by_id('com.cib.wbg:id/mine_headpic_img').click()
    print '点击头像，拍照'
    driver.find_element_by_id('com.cib.wbg:id/personal_change_headpic_layout').click()
    print '点击拍照'
    driver.find_element_by_id('com.cib.wbg:id/take_photo_btn').click()
    print '系统返回键'
    sleep(1)
    driver.keyevent(4)
    print '点击头像，选择照片'
    driver.find_element_by_id('com.cib.wbg:id/personal_change_headpic_layout').click()
    print '点击从手机相册选择'
    driver.find_element_by_id('com.cib.wbg:id/from_gallery_btn').click()
    print '系统返回键'
    sleep(1)
    driver.keyevent(4)
    print '点击头像，取消'
    driver.find_element_by_id('com.cib.wbg:id/personal_change_headpic_layout').click()
    print '点击取消'
    driver.find_element_by_id('com.cib.wbg:id/pop_cancel_btn').click()

    print '点击二维码'
    driver.find_element_by_id('com.cib.wbg:id/personal_change_dbarcode_layout').click()
    print '点击保存至相册'
    driver.find_element_by_id('com.cib.wbg:id/save_to_gallery_btn').click()
    print '点击分享'
    driver.find_element_by_id('com.cib.wbg:id/top_right_imagebtn').click()
    print '系统返回键'
    sleep(1)
    driver.keyevent(4)
    print '返回我的页面'
    sleep(1)
    driver.keyevent(4)
    