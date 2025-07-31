from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver=webdriver.Chrome()

#접속할 주소(네이버 웹툰)
driver.get("https://comic.naver.com/webtoon?tab=thu")

time.sleep(3)
#접속하고 나서 시간을 줌 (사이트 로딩 시간)

#네이버 웹툰 제목 접근
web_class = driver.find_elements(By.CLASS_NAME, 'text')

for c in web_class:
    print(c.text)
print(len(web_class))

time.sleep(10)