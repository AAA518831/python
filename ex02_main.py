# 구구단 함수를 ex02_fun.py에 각각 정의
# main에서 1,2, 번 받아 세로형, 가로형 각각 출력

from ex02_fun import*

run=True
while run:
    num=int(input("메뉴를 선택하세요(0종료) 메뉴번호:  "))
    if num==1:
        v_gugudan()
        # ex02_fun().v_gugudan()

    elif num==2:
        h_gugudan()

    elif num==0:
        print("종료")
        run=False
    else:
        print("선택오류 다시 선택!!")