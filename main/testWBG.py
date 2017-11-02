#coding=utf-8
'''
    测试主流程
    1.config中的wbg.ini控制项目是否执行
'''
from tool.setup import setup
from tool.checkUpdate import checkUpdate
from tool.checkNet import checkNet
from tool.logon import logon
from tool.closeAppium import closeAppium
from tool.exitCode import exitCode
from buttomBtn.testButtomBtn import testButtomBtn
from buttomBtn.clickButtomBtn import clickButtomBtn
from homePage.allHomePageTest import allHomePageTest
from daiBanWenJian.yongYinShenQing import yongYinShenQing
from myPage.allMinePageTest import allMinePageTest
from config.getConfig import getConfig
from time import sleep

pageName='mainWBG.py'

#初始化driver
if getConfig('setup', 'init')=='Y':
    driver=setup() #初始化

#检查是否有更新说明提示框
if getConfig('setup', 'checkUpdate')=='Y':
    checkUpdate(driver) 

#检查网络是否正常
if getConfig('setup', 'checkNet')=='Y':
    checkNet(driver) 

#登录
if getConfig('setup', 'logon')=='Y':
    logonID=getConfig('setup', 'logonID')
    logon(driver,logonID)

#遍历底部5个菜单
if getConfig('test', 'testButtomBtn')=='Y':
    testAllButtomBtn(driver) 

#遍历首页
if getConfig('test', 'allHomePageTest')=='Y':
    clickButtomBtn(driver,'首页') 
    allHomePageTest(driver) 

#遍历我的页面
if getConfig('test', 'allMinePageTest')=='Y':
    clickButtomBtn(driver,'我的') 
    allMinePageTest(driver) 

#OA流程中的用印申请
if getConfig('test', 'yongYinShenQing')=='Y':
    clickButtomBtn(driver,'首页') 
    yongYinShenQing(driver) 

#测试结束
sleep(3)
closeAppium(driver) #关闭模拟器
exitCode() #关闭代码