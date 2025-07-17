#dan=int(input("원하는 단은: "))
#for i in range(1, 10, 1): #1부터 10미만까지 1씩 증가
    #print(f'{dan}*{i}={dan*i}', end="  ")

#1~100까지의 합을 구하여 출력
# sum=0
# for i in range(1, 101, 1): #1부터 101미만(100)까지 1씩 증가
#     sum = sum+i
# print(f"합계는 {sum}")


#하나의 정수를 입력받아 1부터 입력받은 수(a 변수)까지 짝수의 개수를 출력하시오
# sum=0
# cnt=0
# a=int(input("정수 입력> "))
# for i in range(1,a+1): #1~20
#     if i%2==0:
#         cnt=cnt+1
#         sum=sum+i
# print(f"합계는{sum}, 개수는{cnt}입니다.")

 # 아래 예시와 같이 출력하시오
 # *
 # **
 # ***
 # ****
 # *****

# j=1
# for i in range(1,7):
#    print(" ")
#    for j in range(1,i):
#        print("*", end=" ")

j=1
for i in range(1,6):
    for j in range(0,i):
        print("*", end=" ")
    print( )

# *
# **
# ***
# ****
# *****

j=1
for i in range(1,6):
    for j in range(0,6-i): # 초기값이 없으면 1
        print("*", end=" ")
    print( )

for i in range(5, 0, -1): # 5에서 0까지 1씩 감소
    for j in range(0, i):
        print("*", end=" ")
    print( )

# *****
# ****
# ***
# **
# *

