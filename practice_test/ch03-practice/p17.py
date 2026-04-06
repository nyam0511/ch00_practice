"""
실습 17: 점수 처리 프로그램
TODO: 다시 해보기
"""

# 각 점수를 변수에 저장(국어 영어 수학 점수 입력 받기)
kor = int(input("국어 점수: "))
eng = int(input("영어 점수: "))
math = int(input("수학 점수: "))

# 다중 대입으로 과목명을 한 줄에 저장
sub1, sub2, sub3 = "국어", "영어", "수학"

# total = 0 으로 초기화
total = 0

# +=를 사용하여 총점 계산
total += kor
total += eng
total += math

# 평균 계산
avg = total / 3

# 과목 출력
print(f"과목: {sub1} {sub2} {sub3}")
# 각 점수, 총점, 평균 출력
print(f"국어: {kor}")
print(f"영어: {eng}")
print(f"수학: {math}")
print(f"총점: {total}")
print(f"평균: {avg}")