"""
실습 4: 1부터 N까지의 합 구하기
TODO: 다시 해보기
"""

# 숫자 입력받기
n = int(input("숫자를 입력하세요: "))

# 총합
total = 0

# 1부터 입력받은 숫자까지의 합 출력
for i in range(1, n + 1):
    total += i

# 총합 출력
print(f"1부터 {n}까지의 합: {total}")