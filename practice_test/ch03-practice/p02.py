"""
실습 2: 거스름돈 계산
"""

# 물건 가격 입력받기
price = int(input("물건 가격: "))
# 지불 금액 입력받기
paid = int(input("지불 금액: "))
# 지불 금액 - 물건 가격 = 거스름돈 계산
change = paid - price
# 거스름돈 출력
print("거스름돈:", change)
# 거스름돈 // 1000 = 2개
# 남은 거스름돈 = 700
bill_1000 = change // 1000
change = change % 1000
# 거스름돈 // 500 = 1개
# 남은 거스름돈 = 200
coin_500 = change // 500
change = change % 500
# 거스름돈 // 100 = 2개
coin_100 = change // 100
change = change % 100
# ------------------------------------
coin_10 = change // 10
change = change % 10

coin_1 = change // 1

print("1000円:", bill_1000)
print("500円:", coin_500)
print("100円:", coin_100)
# ----------------------------------
print("10円:", coin_10)
print("1円:", coin_1)