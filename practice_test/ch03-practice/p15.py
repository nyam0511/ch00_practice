"""
실습 15: 회원 할인 (삼항 연산자)
"""

# 가격 입력 받기
price = int(input("가격 입력: "))
# 회원 여부 (1: 회원, 0: 비회원) 입력 받기
is_member = int(input("회원 여부 (1: 회원, 0: 비회원): "))

# 회원이면 20% 할인, 비회원이면 5% 할인된 가격 출력
discount = 0.2 if is_member else 0.05

# 할인 계산 = 가격 * (1 - 할인율)
final_price = int(price * (1 - discount))

# 최종 가격 출력
print(f"최종 가격: {final_price}원")