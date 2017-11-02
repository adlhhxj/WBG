#coding=utf-8
'''
    点击坐标，适应不同分辨率
    1.clickImgLocation(driver,location)
'''

from tool.getScreenSize import getScreenSize

def clickImgLocation(driver,location):    
    screenWidth=getScreenSize(driver, 'width')  #获取屏幕宽度，用来适应不同分辨率
    x=location[0].astype(int)  #转换类型，不然tap点击无法使用
    y=location[1].astype(int)
    newx=x*screenWidth/1080  #适应不同分辨率
    newy=y*screenWidth/1080
    driver.tap([(newx,newy)],500)
    