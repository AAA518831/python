#----------------------------------------
# 3글자 이상의 과일 모으기

# fruit=['참외', '파인애플', '사과', '바나나', '골드키위', '배']
# cart = [] # 빈 리스트 선언
# for k in fruit:
#     if len(k) >=3: # 글자 수가 3 이상이면
#         cart.append(k) # 리스트에 추가 / insert = 삽입 / del = 삭제
# print(cart)

#------------------------------------------

과자 = {
    "꼬깔콘": 2000,  #키:값
    "새우깡": 3830,
    "포카칩": 1180,
}
for k,v in 과자.items():
    # 사전의 키-값 튜플 쌍 목록을 표시하는 뷰 객체를 반환합니다.
    print(k,v)

