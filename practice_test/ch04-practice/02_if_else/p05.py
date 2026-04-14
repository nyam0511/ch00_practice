"""
실습 5: 비밀번호 확인
"""

# password 변수에 python123 저장
password = "python123"
# 비밀번호 입력받기
user_input = input("비밀번호를 입력하세요: ")

# 비밀번호가 맞으면 "로그인 성공"
if user_input == password:
    print("로그인 성공")
# 아니면 "비밀번호 오류" "다시 시도하세요" 출력
else:
    print("비밀번호 오류")
    print("다시 시도하세요")