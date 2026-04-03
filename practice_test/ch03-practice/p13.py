"""
실습 13: 합격 여부 (삼항 연산자)
"""

# 점수 입력 받기
score = int(input("점수 입력: "))

# 점수가 70점 이상이면 합격, 아니면 불합격 출력(삼항 연산자)
result = "합격" if score >= 70 else "불합격"
print(result)