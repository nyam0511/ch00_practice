"""
실습 1: 홀짝 판별기
"""

# 숫자 입력받기
num = int(input("숫자를 입력하세요: "))

# 숫자가 홀수인지 짝수인지 출력
# result = "짝수" if num % 2 == 0 else "홀수"
if num % 2 == 0:
    print(str(num) + "은(는) 짝수입니다")
else:
    print(f"{num}은(는) 홀수입니다")