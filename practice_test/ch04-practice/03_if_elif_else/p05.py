"""
실습 5: BMI 판정
TODO: 다시 해보기
"""

# 키 입력받기
height = float(input("키를 입려하세요 (cm): "))
# 몸무게 입력받기
weight = float(input("몸무게를 입력하세요 (kg): "))

# 키(cm)를 m로 변환
height_m = height / 100

# BMI = 몸무게 / 키(m)^2
BMI = weight / (height_m ** 2)

# BMI 18.5 미만: 저체중
if BMI < 18.5:
    body = "저체중"
# BMI 18.5 이상 23 미만: 정상
elif BMI < 23:
    body = "정상"
# BMI 23 이상 25 미만: 과체중
elif BMI < 25:
    body = "과체중"
# BMI 25 이상: 비만
else:
    body = "비만"

# 키(cm) 몸무게 출력
print(f"키: {height}cm, 몸무게: {weight}kg")
# BMI 출력
print(f"BMI: {BMI:.2f}")
# print(f"BMI: {round(BMI, 2)}")
# print("BMI: " + str(round(BMI, 2)))
# 판정 출력
print("판정:", body)
