for i in range(0, 10):
    print(i)
    if(i==4):
        break
print("4이면 탈출\n")

while True: # while(1)
    a=input("종료입력하면 종료됩니다> ")
    if a == "종료":
        break
print("종료되었습니다")
"""
실행시 입력 인자값을 아래와 같이 넣은 후 실행해주세요.
1
2
종료
"""

#파이썬 여러 줄 주석은 작은따옴표(''') 또는 큰따옴표(""")를 세 번 사용