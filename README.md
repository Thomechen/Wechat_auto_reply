# Wechat_auto_reply
Auto comment by filter keyword

# 0.Wechat_auto_reply

此文件為解說微信公眾號自動回覆流程

![0%20Wechat_auto_reply%207a8577667bdc469688ec771b14a3c552/Untitled.png](0%20Wechat_auto_reply%207a8577667bdc469688ec771b14a3c552/Untitled.png)

使用到的模組

```python
from selenium.webdriver.common.keys import Keys #send_keys輸入
from selenium.webdriver.common.action_chains import ActionChains #移動滑鼠
from selenium.webdriver.support.wait import WebDriverWait #等待畫面讀取
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import Chrome #瀏覽器
from selenium.webdriver.chrome.options import Options
import time
```

控制已存在的Chrome瀏覽器

```python
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
chrome_driver = r"D:\Browser\chromedriver_win32\chromedriver.exe" #如果將chrome驅動放到Python目錄，這句可以不要
driver = webdriver.Chrome(chrome_driver, chrome_options=chrome_options)
```

點擊留言管理

![0%20Wechat_auto_reply%207a8577667bdc469688ec771b14a3c552/Untitled%201.png](0%20Wechat_auto_reply%207a8577667bdc469688ec771b14a3c552/Untitled%201.png)

```python
driver.find_element_by_xpath("//*[@title='留言管理']").click()

```

等待網頁網頁讀取

```python
locator = (By.CLASS_NAME,'comment-text')
WebDriverWait(driver,5).until(EC.presence_of_element_located(locator))#等待網頁網取
```

迴圈(由大至小一層一層進入留言區塊)

```python
for i,j,k,l in zip(driver.find_elements_by_xpath("//*[@class='comment-list__item-container']"),
              driver.find_elements_by_class_name('comment-text'),
              driver.find_elements_by_class_name('edit_area'),
              driver.find_elements_by_xpath("//*[@class='weui-desktop-btn weui-desktop-btn_primary']")):
```

建立判斷式(篩選留言內容) 

```python
if '测试' in j.text: # j = driver.find_elements_by_xpath("//*[@class='comment-list__item-container']")
```

移動滑鼠留言區塊

```python
move = ActionChains(driver).move_to_element(j) # j = driver.find_elements_by_xpath("//*[@class='comment-list__item-container']")
move.perform()
```

等待回覆按鈕出現

```python
locator = (By.CLASS_NAME,'icon-reply.comment_opr_meta')
WebDriverWait(driver,5).until(EC.presence_of_element_located(locator))#等待回復按鈕出現
```

點擊回覆按鈕

```python
driver.find_element_by_xpath("//*[@title='回复']").click()
```

等待留言欄位出現

```python
locator = (By.CLASS_NAME,'weui-desktop-btn.weui-desktop-btn_primary')
WebDriverWait(driver,5).until(EC.presence_of_element_located(locator))#等待確認回復按鈕出現
```

輸入留言內容

```python
k.send_keys('自動回復測試') # k = driver.find_elements_by_class_name('edit_area')
```

點擊確認留言按鈕

```python
l.click() # l = driver.find_elements_by_xpath("//*[@class='weui-desktop-btn weui-desktop-btn_primary']")
```

如果未滿足篩選條件則跳過

```python
else:
        continue
```
