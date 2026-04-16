"""
실습 6: 요일 판별
TODO: 다시 해보
"""

# 숫자 입력받기(1~7)
day = int(input("숫자를 입력하세요 (1~7): "))

# 1 이면 1 → 월요일
if day == 1:
    weekend = f"{day} → 월요일"
# 2 이면 2 → 화요일
elif day == 2:
    weekend = "화요일"
# 3 이면 3 → 수요일
elif day == 3:
    weekend = f"{day} → 수요일"
# 4 이면 4 → 목요일
elif day == 4:
    weekend = f"{day} → 목요일"
# 5 이면 5 → 금요일
elif day == 5:
    weekend = f"{day} → 금요일"
# 6 이면 6 → 토요일
elif day == 6:
    weekend = f"{day} → 토요일"
# 7 이면 7 → 일요일
elif day == 7:
    weekend = f"{day} → 일요일"
# 아니면 "잘못된 입력입니다"
else:
    weekend = "잘못된 입력입니다."

# 요일 출력
print(weekend)
