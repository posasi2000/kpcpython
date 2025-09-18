import urllib.request
from bs4  import BeautifulSoup
from selenium import webdriver


# pip install selenium 설치 
# pip install beautifulsoup4 설치  
url = 'https://www.daum.net/'
req = urllib.request.urlopen(url)
first = req.read()
source = first.decode('utf-8')
soup = BeautifulSoup(source, 'html.parser')
print(soup)
import time
time.sleep(2)


# #새로운 항목 기술
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = 'https://www.naver.com/'
driver = webdriver.Chrome()
driver.get(url) #웹브라우저 열기기능
mydata = driver.page_source
driver.find_element(By.NAME, "query").send_keys("파이썬" + Keys.ENTER)
soup  = BeautifulSoup( mydata , 'html.parser')
print(soup)
time.sleep(15)