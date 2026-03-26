"""
실습 4: 합격 판정
"""

# 합격조건
# 점수가 60점 이상이고 100점 이하

# 시험 점수 입력
score = int(input("시험 점수: "))

# 점수 출력
print(f"점수: {score}")
# 60점 이상인가?
up60 = score >= 60
print(f"60점 이상인가? {up60}")

# print("60점 이상인가?", score >= 60)
# 100점 이하인가?
down100 = score <= 100
print(f"100점 이하인가? {down100}")

# print("100점 이하인가?", score <= 100)
# 합격 조건 충족: True or False
cut = up60 and down100
print("합격 조건 충족:", cut)
# print("합격 조건 충족:", up60 and down100)
# print("합격 조건 충족:", score >= 60 and score <= 100)