"""
실습 22: 이벤트 참여 판정
"""

# 회원 여부 (y/n) 입력받기
is_member = input("회원 여부 (y/n): ")
# 나이 입력받기
age = int(input("나이를 입력하세요: "))
# VIP 여부 (y/n) 입력받기
is_vip = input("VIP 여부 (y/n): ")

# 회원이고 (나이가 20세 이사이거나 VIP이면) "이벤트 참여 가능"  출력
can_join = is_member == "y" and (age >= 20 or is_vip == "y")
if can_join:
    print("이벤트 참여 가능")
# 그렇지 않으면 "이벤트 참여 불가" 출력
else:
    print("이벤트 참여 불가")

# -------------------------------------------------------------
# if is_member == "y" and (age >= 20 or is_vip == "y"):
#     print("이벤트 참여 가능")
# # 그렇지 않으면 "이벤트 참여 불가" 출력
# else:
#     print("이벤트 참여 불가")