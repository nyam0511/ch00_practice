"""
실습 21: 로그인 확인
"""

# 로그인 여부 입력받기
is_logged_in = input("로그인 여부 (y/n): ")

# 로그인 상태가 아니면 "로그인이 필요합니다 출력
if not is_logged_in == "y":
    print("로그인이 필요합니다")
# -------------------------------------------
# login = not is_logged_in == "y"
# if login:
#     print("로그인이 필요합니다")