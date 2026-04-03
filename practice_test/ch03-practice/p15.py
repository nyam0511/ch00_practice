"""
실습 15: 회원 할인 (삼항 연산자)
TODO: 다시 해보기
"""

# 가격 입력 받기
price = int(input("가격 입력: "))
# 회원 여부 (1: 회원, 0: 비회원) 입력 받기
is_member = int(input("회원 여부 (1: 회원, 0: 비회원): "))

# 회원이면 20% 할인, 비회원이면 5% 할인된 가격 출력
member = int(price * (1 - 0.2))
no_member = int(price * (1 - 0.05))
result = member if is_member == 1 else no_member
# result = int(price * (1 - 0.2)) if is_member == 1 else int(price * (1 - 0.05))
print(f"최종 가격: {result}원")