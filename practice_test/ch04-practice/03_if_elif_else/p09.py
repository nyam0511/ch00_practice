"""
실습 9: 혈액형 성격
"""

# 혈액형(A/B/O/AB) 입력받기
blood = input("혈액형을 입력하세요 (A/B/O/AB): ")

# AB형: 이성적이고 독창적인 성격
if blood == "AB":
    personality = "이성적이고 독창적인 성격"
# A형: 꼼꼼하고 신중한 성격
elif blood == "A":
    personality = "꼼꼼하고 신중한 성격"
# B형: 자유롭고 창의적인 성격
elif blood == "B":
    personality = "자유롭고 창의적인 성격"
# O형: 사교적이고 리더십이 강한 성격
elif blood == "O":
    personality = "사교적이고 리더십이 강한 성격"
# 그외: "잘못된 입력입니다"
else:
    personality = ""

# 혈액형 출력
# 성격 출력
if personality != "":
    print(f"혈액형: {blood}")
    print(f"성격: {personality}")
# 잘못된 입력이면 "잘못된 입력입니다." 출력
else:
    print("잘못된 입력입니다.")

