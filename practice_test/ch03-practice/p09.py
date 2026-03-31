"""
실습 9: 택시 요금 계산
"""

# 이동 거리 입력받기
distance = int(input("이동 거리(m)를 입력하세요: "))

basic_rate = 4800
basic_distance = 1600
# 추가 거리 = 이동거리 - 최초 거리
add_distance = distance - basic_distance
# 추가요금 = 추가 거리 // 131 * 100
add_charge = (add_distance // 131) * 100
# 택시 요금 = 기본 요금 + 추가 요금
taxi_fare = basic_rate + add_charge

# 이동 거리 출력
print(f"이동 거리: {distance}m")
# 택시 요금 출력
print(f"택시 요금: {taxi_fare}원")

