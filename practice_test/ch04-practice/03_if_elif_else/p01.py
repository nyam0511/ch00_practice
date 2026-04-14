"""
실습 1: 성적 등급
"""

# 점수 입력받기
score = int(input("점수를 입력하세요: "))

# 점수가 90 이상이면 A
if score >= 90:
    grade = "A"
# 점수가 80 이상이면 B 
elif score >= 80:
    grade = "B"
# 점수가 70 이상이면 C 
elif score >= 70:
    grade = "C"
# 점수가 60 이상이면 D
elif score >= 60:
    grade = "D"
# 점수가 60 미만이면 F
else:
    grade = "F"

# 점수 출력
print("점수:", score)
# 등급 출력
print("등급:", grade)

# ------------------------------------------------------

# 점수 출력
# print("점수:", score)

# 점수가 90 이상이면 A 출력
# if score >= 90:
#     print("등급: A")
# 점수가 80 이상이면 B 출력
# elif score >= 80:
#     print("등급: B")
# 점수가 70 이상이면 C 출력
# elif score >= 70:
#     print("등급: C")
# 점수가 60 이상이면 D 출력
# elif score >= 60:
#     print("등급: D")
# 아니면 점수가 60 미만이면 F 출력
# else:
#     print("등급: F")