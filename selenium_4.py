from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#크롬 브라우저 실행
driver=webdriver.Chrome()

#접속할 주소
driver.get("https://search.danawa.com/dsearch.php?k1=%EB%85%B8%ED%8A%B8%EB%B6%81&module=goods&act=dispMain")
# 주소 복사하여 붙이기

#노트북 상품명 접근
notebook_names = driver.find_elements(By.CLASS_NAME, 'prod_name')

for name in notebook_names:
    print(name.text)

time.sleep(10)

