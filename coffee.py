amer_price=2000
cafe_price=3000
capu_price=3500

menu=int(input("1: 아메리카노 2: 카페라떼 3: 카푸치노 => 원하는 메뉴를 선택하세요: "))
if menu == 1:
    americanos=int(input("아메리카노 판매 개수: "))
    coun=americanos*amer_price
elif menu == 2:
    cafelattes=int(input("카페라떼 판매 개수: "))
    coun=cafelattes*cafe_price
else:
    capucinos=int(input("카푸치노 판매 개수: "))
    coun=capucinos*capu_price

# sales=americanos*amer_price
# sales=sales+cafelattes*cafe_price
# sales=sales+capucinos*capu_price

print("총 매출은", coun, "입니다.")
