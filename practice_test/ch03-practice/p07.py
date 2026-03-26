"""
실습 7: 할인 가격 계산
"""

# 총액
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

# 상품 1 = 1200000 * (1 - 0.1)
sale1 = int(price1 * (1 - discount1))
# 상품 2 = 35000 * (1 - 0.2)
sale2 = int(price2 * (1 - discount2))
# 상품 3 = 55000 * (1 - 0.15)
sale3 = int(price3 * (1 - discount3))


# 총액 += 상품 1
total += sale1
# 총액 += 상품 2
total += sale2
# 총액 += 상품 3
total += sale3


# 노트북: 1080000원
print("노트북: " + str(sale1) + "원")
# 마우스: 28000원
print("마우스: " + str(sale2) + "원") 
# 키보드: 46750원
print("키보드: " + str(sale3) + "원")
# 총 결제 금액: ㅇㅇ
print("총 결제 금액: " + str(total) + "원")