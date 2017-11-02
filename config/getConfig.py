#coding=utf-8
'''
    获取配置参数并返回
    1.getConfig(text)，返回参数
'''

from ConfigParser import ConfigParser
import os

def getConfig(text1,text2):
    work_dir=os.path.dirname(os.path.abspath(__file__))
    config_dir=os.path.join(work_dir,'wbg.ini')
    
    config=ConfigParser()
    config.read(config_dir)
    
    result=config.get(text1,text2)
    return result
    print '参数[%s]--%s：%s'%(text1,text2,result)
