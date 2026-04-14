"""
실습 2: 계절 판별
"""

# 월 입력받기
month = int(input("월을 입력하세요 (1~12): "))

# 3 4 5 이면 봄
if 3 <= month <= 5:
    Season = "봄"
# 6 7 8 이면 여름
elif 6 <= month <= 8:
    Season = "여름"
# 9 10 11 이면 가을
elif 9 <= month <= 11:
    Season = "가을"
# 아니면 12 1 2 이면 겨울 
else:
    Season = "겨울"

# 계절 출력
print(f"{month}월은 {Season}입니다.")
# print(str(month) + "월은 " + Season + "입니다.")