"""
실습 8: 윤년 판별
TODO: 한 번 더 해보기
"""

# 연도를 입력 받기
year = int(input("연도를 입력하세요: "))
# 4로 나누어 떨어지면(year % 4 == 0) 윤년
# 100으로 나누어 떨어지면(year % 100 ==0) 윤년 아님
# 400으로 나누어 떨어지면(year % 400 == 0) 윤년
yun = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# yun = (year % 4 == 0 and year % 400 == 0) or (year % 100 == 0 and year % 400 == 0)
     # 2024  4 == 0    100 == 1  false            0    400 == 
# (year % 4 == 0 and year % 100 == 0 and year % 400 == 0)
# yun1 = year % 4 == 0
# yun2 = year % 100 == 0
# yun3 = year % 400 == 0

# yun = (yun1 and yun2 and yun3) and (yun1 and yun3) or (yun1)

print(str(year) + "년은 윤년인가? ", yun)



