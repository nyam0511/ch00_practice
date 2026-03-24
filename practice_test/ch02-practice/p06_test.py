"""
실습 6: 자료형 변환 활용하기
"""

# [1] 아래 두 변수를  숫자로 변환하여 총 금액(price * quantity)출력
price = "4500"
quantity = "3"

price = int(4500)
quantity = int(3)

print(price * quantity)

# [2] 아래 변수들을 문자열로 연결하여 한 줄로 출력
#     출력 형식: "홍길동님의 점수는 95점입니다."

name = "홍길동"
score = 95

print(name + "님의 점수는" + str(score) + "점입니다.")
print(f"{name}님의 점수는 {score}점입니다.")

# [3] 사용자로부터 두 숫자를 입력받아 합계를 출력
#     힌트: input()은 항상 문자열을 반환합니다

num1 = int(input("첫 번째 숫자: "))
num2 = int(input("두 번째 숫자: "))

print("합계: ", num1 + num2)
print(f"합계: {num1 + num2}")