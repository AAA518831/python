#1. total을 0으로 설정한다.
#2. answer를 'yes'로 설정한다.
#3. answer가 'yes'인 동안에 다음을 반복한다
# * 숫자를 입력받는다
# * 숫자를 total에 더한다
# * '계속하실까요? yes/no'를 묻는다
#4. total의 값을 출력한다.
total=0
answer='yes'
while answer == 'yes':
    num=int(input("숫자를 입력하시오>> "))
    total=total+num
    answer=input("계속하시겠습니까?(yes/no)>> ")
print(f"총합은 {total} 입니다")