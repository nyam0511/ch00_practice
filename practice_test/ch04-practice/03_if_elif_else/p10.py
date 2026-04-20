"""
실습 10: 눈코딩
"""

# ── 문제 1 ──
x = 75
if x >= 90:
    print("A")
elif x >= 80:
    print("B")
elif x >= 70:
    print("C")
else:
    print("D")
# 예측: C

# ── 문제 2 ──
num = 0
if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("영")
# 예측: 영

# ── 문제 3 ──
score = 95
if score >= 60:
    print("합격")
elif score >= 90:
    print("우수")
else:
    print("불합격")
# 예측: 합격

# ── 문제 4 ──
age = 15
if age >= 20:
    print("성인")
    print("투표 가능")
elif age >= 14:
    print("청소년")
    print("투표 불가")
else:
    print("어린이")
    print("투표 불가")
# 예측:
# 청소년
# 투표 불가

# ── 문제 5 ──
temp = 35
if temp >= 30:
    print("더움")
if temp >= 20:
    print("따뜻")
if temp >= 10:
    print("선선")
# 예측:
# 더움
# 따뜻
# 선선