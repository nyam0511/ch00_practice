"""
실습 3: 약수 구하기
TODO: 다시 해보기
"""

# 숫자 입력받기
n = int(input("숫자를 입력하세요: "))

total = ""

# 입력받은 숫자 반복
for i in range(1, n + 1):
    # 나눈 나머지가 0이면 약수
    if n % i == 0:
        aliquot = str(i)
        total += " " + aliquot  # " 1"  #f" {aliquot}" 
print("12의 약수:" + total)
# print(total)
# print(f"12의 약수: {total}")
# print(f"12의 약수: {aliquot}")
# print(f"{n}의 약수: {aliquot}")
