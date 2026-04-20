"""
실습 7: 동전 변환
TODO: 다시 해보기
"""

# 금액 입력받기
amount = int(input("금액을 입력하세요 (원): "))

# 총 동전
# all_coin = 0

# 큰 동전(500, 100, 50, 10)부터 몇 개 필요한지 계산

# 500원개수 = 금액 // 500
coin_500 = amount // 500
# 남은 금액 = 금액 % 500
remain_amount = amount % 500

# 나머지 금액을 다음 동전으로 계산

# 100원개수 = 금액 // 100
coin_100 = remain_amount // 100
# 남은 금액 = 금액 % 100
remain_amount = remain_amount % 100

# 50원개수 = 금액 // 50
coin_50 = remain_amount // 50
# 남은 금액 = 금액 % 50
remain_amount = remain_amount % 50

# 10원개수 = 금액 // 10
coin_10 = remain_amount // 10

# 총 동전 수 계산
total = coin_500 + coin_100 + coin_50 + coin_10
# all_coin += coin_500
# all_coin += coin_100
# all_coin += coin_50
# all_coin += coin_10

# 금액 → 동전 변환: 출력
print(f"{amount}원 → 동전 변환:")
# 500원 개수 출력
print("500원: " + str(coin_500) + "개")
# 100원 개수 출력
print("100원:", str(coin_100) + "개")
# 50원 개수 출력
print(f"50원: {coin_50}개")
# 10원 개수 출력
print(f"10원: {coin_10}개")
# 총 돈전 수 출력
print(f"총 동전 수: {total}개")

# ---------------------------------------------

# 각 동전이 0개가 아닐 때만 출력할 때
# 금액 → 동전 변환: 출력
# print(f"{amount}원 → 동전 변환:")
# # 500원 개수
# if coin_500 != 0:
#     print("500원: " + str(coin_500) + "개")
# # 100원 개수
# if coin_100 != 0:
#     print("100원:", str(coin_100) + "개")
# # 50원 개수
# if coin_50 != 0:
#     print(f"50원: {coin_50}개")
# # 10원 개수
# if coin_10 != 0:
#     print(f"10원: {coin_10}개")
# # 총 동전 수
# print(f"총 동전 수: {all_coin}개")

