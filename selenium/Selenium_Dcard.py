import time
from weakref import WeakKeyDictionary
from selenium import webdriver
# import可以模擬鍵盤的模組
from selenium.webdriver.common.keys import Keys
#import explicit wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Path = '/Users/rich/Desktop/Python/Selenium/chromedriver'
driver = webdriver.Chrome(Path)

#輸入爬蟲網址
driver.get('https://www.dcard.tw/f')
#選擇爬蟲用哪個標籤找
Search = driver.find_element_by_name('query')
#先清空搜尋欄避免文字
Search.clear()
#自動輸入文字
Search.send_keys('股票')
#模仿enter
Search.send_keys(Keys.RETURN)
#等瀏覽器做完某個動作,參數是秒數
wait = WebDriverWait(driver, 3)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'sc-28471767-0')))

Titles = driver.find_elements_by_class_name('sc-b57812c2-3')
#用迴圈去跑印出標題
for title in Titles:
    print(title.text)
#回上一頁
driver.back()
#到下一頁
driver.forward()

#停頓5秒
time.sleep(5)
#關閉模擬器
driver.quit()
