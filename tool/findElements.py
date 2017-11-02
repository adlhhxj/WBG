#coding=utf-8
'''
    查找元素，返回元素，并返回查找结果
'''

pageName='findElements.py'

def findElements(driver,method,content):
    print '查找元素，并返回多个值--(%s)'%pageName
    result = []
    flag = None
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
        flag = True
    except:
        print '找不到元素--(%s)'%pageName
        flag = False
        
    result[0] = element
    result[1] = flag
    return result
    