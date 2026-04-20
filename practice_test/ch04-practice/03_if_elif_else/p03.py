"""
실습 3: 교통수단 추천
"""

# 거리 입력받기
distance = float(input("거리를 입력하세요 (km): "))

# 거리가 2km 미만이면 도보
if distance < 2:
    transpor = "도보"
# 거리가 2km 이상 5km 미만이면 자전거
elif distance < 5:
    transpor = "자전거"
# 거리가 5km 이상 20km 미만이면 버스
elif distance < 20:
    transpor = "버스"
# (그 외)20km 이상이면 지하철
else:
    transpor ="지하철"

# 거리 출력
print(f"거리: {distance}km")
# 추천 교통수단 출력
print(f"추천 교통수단: {transpor}")