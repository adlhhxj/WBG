#coding=utf-8

from clickPersonInfo import clickPersonInfo
from clickSheZhi import clickSheZhi
from clickShouCan import clickShouCan
from clickPeiZhi import clickPeiZhi
from clickQianBao import clickQianBao

pageName='allMinePageTest.py'

def allMinePageTest(driver):
    clickPersonInfo(driver)
    clickSheZhi(driver)
    clickShouCan(driver)
    clickPeiZhi(driver)
    clickQianBao(driver)