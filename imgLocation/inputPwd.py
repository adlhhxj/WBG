#coding=utf-8
'''
    密码键盘输入密码
'''
from getImgLocation import getImgLocation
from clickImgLocation import clickImgLocation

def inputPwd(driver,pwd):
    keyboard='sz'  #初始化键盘为数字键盘
    imgPath = 'D:\install\eclipse\workspace\Appium\WBG\imgkeyboard'  #设置图片路径

#点击密码输入框
    imgbg = '%s\\sz1080.png'%imgPath   #背景图
    imgfg = '%s\\szinput-1080.png'%imgPath  #要定位的位置
    location=getImgLocation(imgbg, imgfg)  #返回坐标
    clickImgLocation(driver, location)  #适应不同分辨率，点击坐标
    
#循环输入密码
    for num in pwd:
#判断使用那种键盘
        if (num.isdigit() == True):
            keyboardnew='sz'  #使用数字键盘
        elif (num.isalpha() == True):
            keyboardnew='zm'  #使用字母键盘
        else:
            fh=['~','!','@','#','$','%','^','&','*','(',')','_','+','{','}','|',':','"']  #符号第一页
            fh2=['<','>','?','`','-','=','[',']','\\',';','\'',',','.','/']  #符号第二页
            if num in fh:
                keyboardnew='fh'  #使用符号键盘
            if num in fh2:
                keyboardnew='fh2'
            #以下符号图片命名有变（符号第一页）
            if num=='*':
                num=8
            elif num=='|':
                num=88
            elif num==':':
                num=888
            elif num=='"':
                num=8888
            #以下符号图片命名有变（符号第二页）
            if num == '<':
                num = 8
            elif num == '>':
                num = 88
            elif num == '?':
                num = 888
            elif num == '\\':
                num = 8888
            elif num == '/':
                num = 88888

#判断是否切换键盘
        if (keyboard != keyboardnew):  #判断是否使用新键盘
            #当前已在符号第二页fh2，跳转到其他页
            if (keyboard == 'fh2'):  
                #跳转到符号第一页fh，以便使用
                imgbg = '%s\\%s1080.png'%(imgPath,keyboard)  #当前fh2键盘背景图片
                imgbtn='%s\\%s%s-1080.png'%(imgPath,keyboard,'left')  #当前键盘left键
                location = getImgLocation(imgbg,imgbtn)  #获取left坐标
                clickImgLocation(driver, location)  #点击坐标
                if (keyboardnew == 'fh'):
                    keyboard=keyboardnew  #更新正在使用的键盘
                #跳转到数字sz 或 字母zm页面
                else:
                    imgbg = '%s\\%s1080.png'%(imgPath,'fh')  #当前fh键盘（left键执行后）
                    imgbtn='%s\\%s%sbtn-1080.png'%(imgPath,'fh',keyboardnew)  #切换键图片
                    location = getImgLocation(imgbg,imgbtn)  #旧键盘背景图片上按键的坐标
                    clickImgLocation(driver, location)  #点击坐标
                    keyboard=keyboardnew  #更新正在使用的键盘
            
            #当前不在符号第二页fh2，跳转到其他页
            else:  
                #当前在符号第一页fh，而且要跳转到符号第二页fh2
                if(keyboard == 'fh'):
                    if(keyboardnew == 'fh2'):
                        imgbg = '%s\\%s1080.png'%(imgPath,keyboard)  #当前旧键盘背景图片
                        imgbtn='%s\\%s%s-1080.png'%(imgPath,keyboard,'right')  #旧键盘背景图片上切换键图片
                        location = getImgLocation(imgbg,imgbtn)  #旧键盘背景图片上按键的坐标
                        clickImgLocation(driver, location)  #点击坐标
                        keyboard=keyboardnew  #更新正在使用的键盘
                    #当前在符号第一页fh，而且要跳到数字sz 或 字母zm页
                    else:
                        imgbg = '%s\\%s1080.png'%(imgPath,keyboard)  #当前旧键盘背景图片
                        imgbtn='%s\\%s%sbtn-1080.png'%(imgPath,keyboard,keyboardnew)  #旧键盘背景图片上切换键图片
                        location = getImgLocation(imgbg,imgbtn)  #旧键盘背景图片上按键的坐标
                        clickImgLocation(driver, location)  #点击坐标
                        keyboard=keyboardnew  #更新正在使用的键盘
                #当前不在符号第一、第二页，跳转到其他页
                else:
                    #跳转到符号第二页
                    if(keyboardnew == 'fh2'):
                        #先跳转到符号第一页
                        imgbg = '%s\\%s1080.png'%(imgPath,keyboard)  #当前旧键盘背景图片
                        imgbtn='%s\\%s%sbtn-1080.png'%(imgPath,keyboard,'fh')  #旧键盘背景图片上切换键图片
                        location = getImgLocation(imgbg,imgbtn)  #旧键盘背景图片上按键的坐标
                        clickImgLocation(driver, location)  #点击坐标
                        #再跳转到符号第二页
                        imgbg = '%s\\%s1080.png'%(imgPath,'fh')  #当前旧键盘背景图片
                        imgbtn='%s\\%s%s-1080.png'%(imgPath,'fh','right')  #旧键盘背景图片上切换键图片
                        location = getImgLocation(imgbg,imgbtn)  #旧键盘背景图片上按键的坐标
                        clickImgLocation(driver, location)  #点击坐标
                        keyboard=keyboardnew  #更新正在使用的键盘
                    #在sz、zm页跳转到sz、zm、fh页
                    else:
                        imgbg = '%s\\%s1080.png'%(imgPath,keyboard)  #当前旧键盘背景图片
                        imgbtn='%s\\%s%sbtn-1080.png'%(imgPath,keyboard,keyboardnew)  #旧键盘背景图片上切换键图片
                        location = getImgLocation(imgbg,imgbtn)  #旧键盘背景图片上按键的坐标
                        clickImgLocation(driver, location)  #点击坐标
                        keyboard=keyboardnew  #更新正在使用的键盘

#输入一个密码值
        imgbg = '%s\\%s1080.png'%(imgPath,keyboard)  #当前键盘背景图片（若有更新）
        imgkb = '%s\\%s%s-1080.png'%(imgPath,keyboard,num)  #当前键盘上的按键图片
        location = getImgLocation(imgbg,imgkb)  #当前键盘上的按键坐标
        clickImgLocation(driver, location)

#密码键盘上点击确定，结束密码输入
    imgkb = '%s\\%s%s-1080.png'%(imgPath,keyboard,'confirm')  #当前键盘上的确定按钮图片
    location = getImgLocation(imgbg,imgkb)  #当前键盘上的按键坐标
    clickImgLocation(driver, location)
    