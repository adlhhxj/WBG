#coding=utf-8
'''
    查找元素，返回元素
'''
pageName='findElement.py'

def findElement(driver,method,content):
    print '查找元素--(%s)'%pageName
    try:
        if (method == 'id'):
            element = driver.find_element_by_id(content)
        elif (method == 'ids'):
            element = driver.find_elements_by_id(content)
        elif (method == 'name'):
            element = driver.find_element_by_name(content)
        elif (method == 'names'):
            element = driver.find_elements_by_name(content)
        elif (method == 'text'):
            element = driver.find_element_by_tag_name(content)
        elif (method == 'class'):
            element = driver.find_element_by_class_name(content)
        elif (method == 'classes'):
            element = driver.find_elements_by_class_name(content)
    except:
        print '找不到元素--(%s)'%pageName
    return element
