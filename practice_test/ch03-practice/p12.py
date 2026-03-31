"""
실습 12: 복합 조건식
"""

# 점수 입력 받기
score = int(input("점수 입력: "))
# 출석률 입력 받기
attendance = int(input("출석률 입력: "))

# 점수가 80점 이상이고 출석률이 90 초과이면 수료 가능 출력
if score >= 80 and attendance > 90:
    print("수료 가능")
# 그렇지 않으면 수료 불가 출력
else:
    print("수료 불가")