"""
실습 3: 할인 적용
"""

# 회원 여부 입력받기
is_member = input("회원이신가요? (Y/N): ")

# 회외이면("Y"이면)
if is_member == "Y":
    # VIP 여부 입력받기
    vip = input("VIP 회원이신가요? (Y/N): ")
    # VIP이면("Y"이면) "20% 할인 적용"
    if vip == "Y":
        print("20% 할인 적용")
    # VIP가 아니면 "10% 할인 적용"
    else:
        print("10% 할인 적용")
# 비회원이면 "할인 없음"
else:
    print("할인 없음")