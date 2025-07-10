# 숫자(점수) 3개를 input으로 입력
# 숫자는 list(0~2번째 방에 저장)
# 총점, 평균 구하여 출력

# score=[0, 0, 0]
# score[0]=int(input("국어 점수를 입력하세요: "))
# score[1]=int(input("수학 점수를 입력하세요: "))
# score[2]=int(input("영어 점수를 입력하세요: "))
score=[]
score.append(int(input("국어 점수 입력: ")))
score.append(int(input("수학 점수 입력: ")))
score.append(int(input("영어 점수 입력: ")))
# tot=score[0]+score[1]+score[2]
tot=sum(score)
avg=round(tot/3, 2) #정수와 정수 -> 실수가 나올 수도 있음

print("총점은", tot, "입니다.")
print("평균은", avg, "입니다.")