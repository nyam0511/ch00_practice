"""
실습 16: 파일 크기 표시 (삼항 연산자)
"""

# 파일 크기(바이트) 입력 받기
size = int(input("파일 크기(바이트) 입력: "))

# 1024 이상이면 KB 단위로, 아니면 B 단위로 출력
result = f"{size / 1024:.1f}KB" if size >= 1024 else f"{size}B"
# 파일 크기 출력
print("파일 크기:", result)
