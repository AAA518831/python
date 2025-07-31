# 판다스(pandas) 라이브러리 설치 : pip install pandas

import pandas as pd #pd라고 명명
# 판다스(pandas) 라이브러리 설치

# 시리즈(1차원) 선언
series1=pd.Series([2,4,6,8,10]) #인덱스는 0부터
print(series1)

# 성적 다루는 간단한 예제

num=[1,2,3,4,5]
score_java=pd.Series([98,76,60,85,80], index=num) # index가 1~5
score_python=pd.Series([88,92,100,55,70], index=num)

print(score_java)
print(score_python)

# java, python 시리즈 합계
total = score_java + score_python
print("덧셈 결과는")
print(total)
#index 끼리 각각 연산

print("index 기준 내림차순 정렬")
print(total.sort_index(ascending=False))
print("# 값 기준 오름차순 정렬")
print(total.sort_values(ascending=True)) # 기본값으로 생략 가능
print("값 기준 내림차순 정렬")
print(total.sort_values(ascending=False))

t1= total.sort_values(ascending=True)
t1.to_csv('./res01.csv')