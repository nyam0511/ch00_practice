"""
실습 5: BMI 판정
"""

# 키 입력받기
height = float(input("키를 입력하세요 (cm): "))
# 몸무게 입력받기
weight = float(input("몸무게를 입력하세요 (kg): "))

# 키(cm)를 키(m)로 변환
height_m = height / 100

# BMI 계산(몸무게 / 키(m)^2)
bmi = weight / (height_m ** 2)

# BMI 18.5 미만: 저체중
if bmi < 18.5:
    result = "저체중"
# BMI 18.5 이상 23 미만: 정상
elif bmi < 23:
    result = "정상"
# BMI 23 이상 25 미만: 과체중
elif bmi < 25:
    result = "과체중"
# BMI 25 이상: 비만
else:
    result = "비만"

# 키, 몸무게 출력
print(f"키: {height}, 몸무게: {weight}")
# BMI 출력(소수점 2자리까지만)
print(f"BMI: {bmi:.2f}")
# print("BMI:", round(bmi, 2))
# 판정 출력
print("판정:", result)