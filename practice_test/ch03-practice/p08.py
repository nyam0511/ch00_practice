"""
실습 8: 윤년 판별
"""

# 연도 입력받기
year = int(input("연도를 입력하세요: "))

# 윤년 계산
leap_year = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
# year년은 윤년인가? leap_year
print(f"{year}은 윤년인가? {leap_year}")

