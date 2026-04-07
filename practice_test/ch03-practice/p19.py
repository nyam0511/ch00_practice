"""
실습 19: 수료 판정
"""

# 점수 입력받기
score = int(input("점수를 입력하세요: "))
# 출석률 입력받기
attendance = int(input("출석률을 입력하세요: "))

# 점수 출력
print("점수:", score)
# 출석률 출력
print("출석률:", attendance)

# 점수가 80점 이상이고 출석률이 90을 초과하면 "수료 가능" 출력
test_pass = score >= 80 and attendance > 90

if test_pass:
    print("수료 가능")
# 그렇지 않으면 "수료 불가" 출력
else:
    print("수료 불가")
# --------------------------------------------
# if score >= 80 and attendance > 90:
#     print("수료 가능")
# # 그렇지 않으면 "수료 불가" 출력
# else:
#     print("수료 불가")