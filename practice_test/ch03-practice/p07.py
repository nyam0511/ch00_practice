"""
실습 7: 할인 가격 계산
"""
# TODO: 다시 하셈 ㅇㅇ

total = 0

# 상품 1: 노트북 1200000원, 10% 할인
price1 = 1200000
discount1= 0.1

# 상품 2: 마우스 35000원, 20% 할인
price2 = 35000
discount2 = 0.2

# 상품 3: 키보드 55000원, 15% 할인
price3 = 55000
discount3 = 0.15
# 할인 가격1 = 1200000 * (1 - 0.1)
price_discount1 = price1 * (1 - discount1)
# 할인 가격2 = 35000 * (1 - 0.2)
price_discount2 = price2 * (1 - discount2)
# 할인 가격3 = 55000 * (1 - 0.15)
price_discount3 = price3 * (1 - discount3)
# 총액 계산
print(f"노트북: {int(price_discount1)}원")
print(f"마우스: {int(price_discount2)}원")
print(f"키보드: {int(price_discount3)}원")

price_discount1 += price_discount2
price_discount1 += price_discount3
print(f"총 결제 금액: {int(price_discount1)}원")


