"""
실습 4: 영화 요금 계산
TODO: 다시 해보기
"""

# 나이 입력받기
age = int(input("나이를 입력하세요: "))

# 7세 이하: 무료 (0원)
if age <= 7:
    rate = "무료"
    fare = "0"
# 8세 ~ 13세: 어린이 (5,000원)
elif age <= 13:
    rate = "어린이"
    fare = "5,000"
# 14세 ~ 19세: 청소년 (8,000원)
elif age <= 19:
    rate = "청소년"
    fare = "8,000"
# 20세 ~ 64세: 성인 (12,000원)
elif age <= 64:
    rate = "성인"
    fare = "12,000"
# 65세 이상: 경로 (5,000원)
else:
    rate = "경로"
    fare = "5,000"

# 나이 출력
print("나이:", str(age) + "세")
# 구분 출력
print(f"구분: {rate}")
# 요금 출력
print(f"요금: {fare}원")
