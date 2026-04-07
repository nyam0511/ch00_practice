"""
실습 20: 입장 판정
"""

# 나이 입력받기
age = int(input("나이를 입력하세요: "))
# 보호자 동반 여부 (y/n) 입력받기
guardian = input("보호자 동반 여부 (y/n): ")

# 나이 출력
print("나이:", age)
# 보호자 동반 여부 출력
print(f"보호자 동반: {guardian}")

# 나이가 20세 이상이거나 보호자가 동반된 경우 "입장 가능" 출력
position = age >= 20 or guardian == "y"
if position:
    print("입장 가능")
# 그렇지 않으면 "입장 불가" 출력
else:
    print("입장 불가")

# ---------------------------------
# if age >= 20 or guardian == "y":
#     print("입장 가능")
# # 그렇지 않으면 "입장 불가" 출력
# else:
#     print("입장 불가")

