# 크롤링(crawling)은 웹페이지를 그대로 가져와서 거기서 데이터를 추출해내는 행위
#  selenium : 동적 크롤링 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver=webdriver.Chrome()
#접속할 주소
driver.get("https://www.naver.com")
#검색창 접근
time.sleep(2)
search_element=driver.find_element(By.XPATH, '//*[@id="query"]')

#검색어 입력
search_element.send_keys("오늘날씨")
time.sleep(2)

#검색버튼 클릭
btn=driver.find_element(By.XPATH, '//*[@id="search-btn"]')
btn.click()

time.sleep(10)