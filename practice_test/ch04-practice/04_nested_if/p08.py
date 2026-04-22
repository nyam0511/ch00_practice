"""
실습 8: 주문 처리
"""

# 주문 방식 입력받기
order_type = input("주문 방식을 입력하세요 (배달/포장): ")
# 음식 가격 저장
price = 15000

# 주문 방식이 배달이면
if order_type == "배달":
    # 거리를 입력받기
    distance = float(input("거리를 입력하세요(km): "))
    # 거리가 3km 이하: 배달비 2000원
    if distance <= 3:
        delivery_fee = 2000
    # 거리가 3km 초과: 배달비 3500원
    else:
        delivery_fee = 3500
    # 합계 = 음식 + 배달비
    pay = price + delivery_fee
    # 출력: "배달 주문: 음식 15000원 + 배달비 {배달비}원 = 총 {합계}원"
    print(f"배달 주문: 음식 {price}원 + 배달비 {delivery_fee}원 = 총 {pay}원")
# 주문 방식이 포장이면
elif order_type == "포장":
    # 포장 할인 2000원 적용
    package_discount = 2000
    # 합계 = 음식 - 포장 할인
    pay = price - package_discount
    # 출력: "포장 주문: 음식 15000원 - 할인 2000원 = 총 13000원"
    print(f"포장 주문: 음식 {price}원 - 배달비 {package_discount}원 = 총 {pay}원")
# 그외: "잘못된 주문 방식입니다."
else:
    print("잘못된 주문 방식입니다.")