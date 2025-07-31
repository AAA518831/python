from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

def scroll_fun():
    while True:
    #스크롤하기 전 높이
        h1= driver.execute_script("return document.documentElement.scorllHeight")
        #print("첫 번째 높이", h1)
    #스크롤을 현재높이 만큼 내리기
        driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    #영상 로딩 시간(잠시 대기)
        time.sleep(2)
    #스크롤 내린 뒤 높이 값
        h2=driver.execute_script("return document.documentElement.scrollHeight")
        #print("두 번째 높이", h2)
    #스크롤 전, 후 높이 비교
        if h1==h2:
            break

#크롬 브라우저 실행
driver=webdriver.Chrome()
driver.get("https://www.youtube.com/")

time.sleep(2)
#검색창 요소 접근
search_input=driver.find_element(By.CSS_SELECTOR, 'input[name="search_query"]')
#<input> 태그이면서 name="search_query"인 요소

# 검색어 입력
search_input.send_keys("데몬헌터스")
# 엔터 치기
search_input.send_keys(Keys.RETURN)

#무한 스크롤 함수 호출
scroll_fun() # 함수 정의를 상단에서 한 이후 제목요소 다져오기 전에 호출

# 제목 요소 가져오기
titles=driver.find_elements(By.XPATH,'//*[@id="video-title"]')

#제목 저장을 위한 리스트
title_list=[]

for title in titles:
    if title.get_attribute("aria-label") and title.text:
        title_list.append(title.text)

#제목 리스트가 담긴 딕셔너리
c_result={
    "title":title_list,
}

#딕셔너리를 dataFrame로
result=pd.DataFrame(c_result)
#Dataframe을 csv로 저장
result.to_csv("./result1.csv", encoding="utf-8-sig")

# 조회수 내림차순 정렬후 csv 저장
result.sort_values(by=["title"], ascending=False).to_csv("./result2.csv", encoding="utf-8-sig")