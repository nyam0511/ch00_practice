"""
실습 8: 나만의 파스타 만들기
"""

# 변수 pasta에 "파스타" 저장
pasta = "파스타"

# 치즈 추가 여부 입력받기
add_cheese = input("치즈를 추가할까요? (예/아니오): ")
# 베이컨 추가 여부 입력받기
add_bacon = input("베이컨을 추가할까요? (예/아니오): ")
# 새우 추가 여부 입력받기
add_shrimp = input("새우를 추가할까요? (예/아니오): ")

# pasta = "파스타"
# 치즈 추가이면 pasta에 " + 치즈"
if add_cheese == "예":
    pasta += " + 치즈"
# 베이컨 추가이면 pasta에 " + 베이컨" 
if add_bacon == "예":
    pasta += " + 베이컨"
# 새우 추가이면 pasta에 " + 새우"
if add_shrimp == "예":
    pasta += " + 새우"

# 최종 pasta 변수 출력
print("나의 파스타: " + pasta)