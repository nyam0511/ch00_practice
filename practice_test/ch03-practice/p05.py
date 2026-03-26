"""
실습 5: BMI 계산기
"""

# 키(cm) 입력
height = int(input("키(cm)를 입력하세요: "))
# 몸무게(kg) 입력
weight = int(input("몸무게(kg)를 입력하세요: "))
# 키 출력
print(f"키: {height}cm")
# 몸무게 출력
print(f"몸무게: {weight}kg")
# 키 = 키 / 100
height = height / 100
# BMI = 몸무게 / 키의 제곱
print(f"BMI: {weight / height ** 2}")