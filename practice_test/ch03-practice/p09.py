"""
실습 9: 택시 요금 계산
TODO: 한 번 더 해보기
"""

# 이동 거리 입력받기
distance = int(input("이동 거리(m)를 입력하세요: "))

# 기본요금: 4800원
basic_fee = 4800
base_dist = 1600
# 초과(excess) 거리 = 이동 거리 - 1600m
excess_distance = distance - base_dist

# 추가요금 = (초과 거리 // 131) * 100
add_charge = (excess_distance // 131) * 100

# 택시 요금 = 추가 요금 + 기본 요금
taxi_fare = basic_fee + add_charge

print("이동 거리:", str(distance) + "m")
print("택시 요금:", str(taxi_fare) + "원")
