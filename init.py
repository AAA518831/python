x = input("이름의 첫 번째 글자를 입력하시오: ")
y = input("이름의 두 번째 글자를 입력하시오: ")
z = input("이름의 세 번째 글자를 입력하시오: ")
print(x)
print(type(x))
init= x[0]+y[0]+z[0]
# print("\n영어 이니셜은", init,"입니다.")
print(f"\n영어 이니셜은{init}입니다.")