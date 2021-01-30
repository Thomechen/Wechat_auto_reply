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
import os

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_options.add_argument("'user-agent'='Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166'")
chrome_driver = r"C:\Users\islan\Desktop\Wechat_auto_reply\chromedriver.exe" #如果將chrome驅動放到Python目錄，這句可以不要
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)

# for i in driver.find_elements_by_xpath("//div[@class='comment-list__item']/div[@class='comment-list__item-container']"):
#     print(i.text)


# stop1 = 6 #設定回復幾則留言,由上到下
for j,k,l in zip(driver.find_elements_by_xpath("//div[@class='comment-list__item']"),
              driver.find_elements_by_class_name('edit_area'),
              driver.find_elements_by_xpath("//*[@class='weui-desktop-btn weui-desktop-btn_primary']")): #主要留言

    if '测试' in j.text : #關鍵字篩選
        move = ActionChains(driver).move_to_element(j)
        move.perform()

        locator = (By.CLASS_NAME,'icon-reply.comment_opr_meta')
        WebDriverWait(driver,1).until(EC.presence_of_element_located(locator))#等待回復按鈕出現

        driver.find_element_by_xpath("//*[@title='回复']").click()

        locator = (By.CLASS_NAME,'weui-desktop-btn.weui-desktop-btn_primary')
        WebDriverWait(driver,1).until(EC.presence_of_element_located(locator))#等待確認回復按鈕出現

        k.send_keys('自動回復測試')

        l.click()

        time.sleep(1)
    else:
        continue


    
print('Done')
