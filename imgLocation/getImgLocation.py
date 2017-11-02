#coding=utf-8
'''
    获取图片坐标
    1.getImgLocation(imbg,imfg)
        imbg：背景大图
        imfg：要找的前景小图
        返回坐标信息
'''
import cv2
import numpy as np

def getImgLocation(imbg,imfg):
    img_rgb = cv2.imread(imbg)
    template = cv2.imread(imfg)
    res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
    threshold = .95    # 匹配度参数，1为完全匹配
    loc = np.where(res >= threshold)
    position = zip(*loc[::-1])[0]
    return position
    
