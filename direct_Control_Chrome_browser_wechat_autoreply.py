# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 00:22:45 2021

@author: islan
"""
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"D:\Browser\chromedriver_win32\chromedriver.exe" #如果將chrome驅動放到Python目錄，這句可以不要
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

driver.find_element_by_xpath("//*[@title='留言管理']").click()
locator = (By.CLASS_NAME,'comment-text')
WebDriverWait(driver,5).until(EC.presence_of_element_located(locator))#等待網頁網取

# stop1 = 6 #設定回復幾則留言,由上到下
for i,j,k,l in zip(driver.find_elements_by_xpath("//*[@class='comment-list__item-container']"),
              driver.find_elements_by_class_name('comment-text'),
              driver.find_elements_by_class_name('edit_area'),
              driver.find_elements_by_xpath("//*[@class='weui-desktop-btn weui-desktop-btn_primary']")): #主要留言
    if '测试' in j.text: #關鍵字篩選
        move = ActionChains(driver).move_to_element(j)
        move.perform()
    
        locator = (By.CLASS_NAME,'icon-reply.comment_opr_meta')
        WebDriverWait(driver,5).until(EC.presence_of_element_located(locator))#等待回復按鈕出現
            
        driver.find_element_by_xpath("//*[@title='回复']").click()
        
        locator = (By.CLASS_NAME,'weui-desktop-btn.weui-desktop-btn_primary')
        WebDriverWait(driver,5).until(EC.presence_of_element_located(locator))#等待確認回復按鈕出現
        
        k.send_keys('自動回復測試')
    
        l.click()
        
        # time.sleep(2)
    else:
        continue
    
# print(driver.title)
print('Done')
