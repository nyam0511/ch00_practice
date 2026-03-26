"""
실습 6:시간 변환
"""

# 초 입력받기
second1 = int(input("초를 입력하세요: "))
# 시간 = 초 // 3600
hour = second1 // 3600
# 초(125) = 초 % 3600
minute_f = second1 % 3600 
# 분 = 초(125) // 60
minute = minute_f // 60 #2
second2 = minute_f % 60
# 초(5) = 초(125) % 60 
print(str(second1) + "초")
print("= " + str(hour) + "시간 " + str(minute) + "분 " + str(second2) + "초")
# print(f"= {hour}시간 {minute}분 {second2}초")


