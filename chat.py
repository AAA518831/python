print("안녕하세요?\n")
name= input('이름이 어떻게 되시나요? ')
print(f'\n만나서 반갑습니다 {name}씨.')
print('이름의 길이는 다음과 같군요:'+str(len(name)))
# print('이름의 길이는 다음과 같군요:',len(name))
# +는 문자+문자 연결 의미
# len(name)-> 글자수->숫자->str(숫자)->문자로
age= int(input("나이가 어떻게 되나요? "))
# input 은 기본이 문자
print(f"내년이면 {str(age+1)}이 되시는군요.")
addr= input("주소가 어떻게 되나요? ")
addr2= addr.split() # 인천 남동구 구월동
# 기본적으로 공백을 기준으로 문자열을 나눔
print(f"{addr2[2]} 지역에 사시는군요")