# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 19:35:44 2021

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
open_chrome = os.system('chrome.exe --remote-debugging-port=9223 --user-data-dir="C:\selenum\AutomationProfile"')
class auto_comment():
      
    def control_chrome(self,url = 'https://www.google.com.tw'):
        self.chrome_options = Options()
        self.chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9223")
        self.chrome_driver = r"C:\Users\islan\Desktop\Wechat_auto_reply\chromedriver.exe" #如果將chrome驅動放到Python目錄，這句可以不要
        self.driver = webdriver.Chrome(self.chrome_driver, chrome_options=self.chrome_options)
        self.driver.get(url)

wechat = auto_comment()

wechat.control_chrome()