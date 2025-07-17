# for i in [1,2,3,4,5]: #끝에 :이 있어야 함
#     print("방문을 환영합니다.") #들여쓰기 해야 함
# for i in [1,2,3,4,5]:
#     print("i=", i)
# a=100
# b=200
# print(a,b,sep="와", end="  끝")
# print(a,b, end="  ") #줄바꿈하지 않고 옆으로 출력

import turtle
t=turtle.Turtle()

for count in range(6):
    t.circle(100)
    t.left(360/6)