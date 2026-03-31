"""
실습 7: 할인 가격 계산
"""

# 총액 = 0
total = 0
# 상품 1: 노트북 1200000원, 10% 할인
price1 = 1200000
discount1 = 0.1
# 상품 2: 마우스 35000원, 20% 할인
price2 = 35000
discount2 = 0.2
# 상품 3: 키보드 55000원, 15% 할인
price3 = 55000
discount3 = 0.15

# 상품 1 할인 가격 계산
sale1 = int(price1 * (1 - discount1))
# 상품 2 할인 가격 계산
sale2 = int(price2 * (1 - discount2))
# 상품 3 할인 가격 계산
sale3 = int(price3 * (1 - discount3))

# 총액 구하기
# 총액 += 상품 1할
total += sale1
# 총액 += 상품 2할
total += sale2
# 총액 += 상품 3할
total += sale3

# 노트북 할인 가격
print(f"노트북: {sale1}원")
# 마우스 할인 가격
print("마우스:", str(sale2) + "원")
# 키보드 할인 가격
print(f"키보드: {sale3}원")
# 총 결제 금액
print(f"총 결제 금액: {total}원")
