num=input("주민등록번호: ") 

#split() 함수를 사용하여 문자열을 하이픈(-)을 기준으로 나눈 후,
#두 번째 부분을 가져옴, 리스트 만듬

num=num.split("-")[1] #주민번호 뒷자리만 추출
print("추출문자열:", num)

if num[0]== "1" or num[0]== "3":
    print("남자")
else :
    print("여자")

#addr.split() : 공백중심으로 분리