"""
실습 4: 합격 판정
"""

# 시험 점수를 입력 받기
score = int(input("시험 점수: "))

# 시험 점수 출력
print(f"점수: {score}")

# 60점 이상인가? True or False
print("60점이상인가?", score >= 60)
# 100점 이하인가? True or False
print("100점 이하인가?", score <= 100)
# 합격 조건 충족: True or False
print("합격 조건 충족:", score >= 60 and score <=100)