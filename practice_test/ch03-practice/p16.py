"""
실습 16: 파일 크기 표시 (삼항 연산자)
TODO: 다시 해보기
"""

# 파일 크기(바이트) 입력 받기
size = int(input("파일 크기(바이트) 입력: "))

# 파일 크기 = 1024 이상이면 KB 단위로 아니면 B 단위로 출력
file_size = f"{size / 1024:.1f}KB" if size >= 1024 else f"{size}B"
print(f"파일 크기: {file_size}")
