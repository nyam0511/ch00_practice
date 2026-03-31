"""
실습 5: BMI 계산기
"""

# 키 입력 받기
height = int(input("키(cm)를 입력하세요: "))
# 몸무게 입력받기
weight = int(input("몸무게(kg)를 입력하세요: "))

# 키(cm) -> 키(m) 변환, 제곱
height_m = (height / 100) ** 2
# BMI계산: 몸무게 / 키의 제곱
BMI = weight / height_m

# 키 출력
print("키:", height)
# 몸무게 출력
print("몸무게:", weight)
# BMI 출력
print("BMI:", BMI)