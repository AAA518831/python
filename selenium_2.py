# 크롤링(crawling)은 웹페이지를 그대로 가져와서 거기서 데이터를 추출해내는 행위
#  selenium : 동적 크롤링 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver=webdriver.Chrome()
#접속할 주소
driver.get("https://www.naver.com")

# 동적인 동작
# 로그인 버튼 xpath 접근 (원하는 내용을 오른쪽버튼->복사->xpath복사)
login_button=driver.find_element(By.XPATH, '//*[@id="account"]/div/a')

# 로그인 버튼 클릭
login_button.click()

time.sleep(10)