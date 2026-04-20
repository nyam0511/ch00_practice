"""
실습 6: 요일 판별
"""

# 숫자 입력받기
day = int(input("숫자를 입력하세요 (1~7): "))

# 1이면 월요일
if day == 1:
    week = "월요일"
# 2이면 화요일
elif day == 2:
    week = "화요일"
# 3이면 수요일
elif day == 3:
    week = "수요일"
# 4이면 목요일
elif day == 4:
    week = "목요일"
# 5이면 금요일
elif day == 5:
    week = "금요일"
# 6이면 토요일
elif day == 6:
    week = "토요일"
# 7이면 일요일
elif day == 7:
    week = "일요일"
# 그외: "잘못된 입력입니다."
else:
    week = ""

# 숫자 → 요일 출력
# 잘못된 입력이면 잘못된 입력입니다 출력
if week != "":
    print(f"{day} → {week}")
else:
    print("잘못된 입력입니다.")
