"""
실습 2: 거스름돈 계산
"""

# 물건 가격 입력 받기
price = int(input("물건 가격: "))
# 지불 금액 입력 받기
paid = int(input("지불 금액: "))

# 거스름돈 = 지불 금액 - 물건 가격
change = paid - price
# 거스름돈 출력
print("거스름돈: " + str(change) + "원")
# 1000원 개수 = 거소름돈 // 1000
bill_1000 = change // 1000
# 거스름돈 = 거스름돈 % 1000
change1 = change % 1000

# 500원 개수 = 거스름돈 // 500
coin_500 = change1 // 500
# 거스름돈 = 거스름돈 % 500
change1 = change1 % 500

# 100원 개수 = 거스름돈 // 100
coin_100 = change1 // 100

# 1000원 개수 출력
print("1000원: " + str(bill_1000) + "개")
# 500원 개수 출력
print("500원:", str(coin_500) + "개")
# 100원 개수 출력
print("100원:", str(coin_100) + "개")