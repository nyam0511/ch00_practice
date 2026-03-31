"""
실습 6: 시간 변환
"""

# 초 입력받기
seconds = int(input("초를 입력하세요: "))

# 시간 = 초 // 3600
hour = seconds // 3600
# 나머지 = 초 % 3600
time = seconds % 3600

# 분 = 나머지 // 60
minutes = time // 60
# 초2 = 나머지 % 60
secs = time % 60

# 입력받은 초 출력
print(f"{seconds}초")
#  시간 분 초 출력
# print("=", str(hour) + "시간", str(minutes) + "분", str(secs) + "초")
print(f"= {hour}시간 {minutes}분 {secs}초")