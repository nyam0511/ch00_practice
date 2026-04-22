"""
실습 4: 배송 방식
"""

# 무게(kg) 입력받기
weight = float(input("무게를 입력하세요(kg): "))

# 무게가 2kg 이상이면
if weight >= 2:
    # 빠른 배송 선택 여부 입력받기 (Y/N)
    quick_delivery = input("빠른 배송입니까? (Y/N): ")
    # 빠른 배송이면 "택배(빠른 배송) - 5000원"
    if quick_delivery == "Y":
        print("택배(빠른 배송) - 5000원")
    # 빠른 배송이 아니면 "택배(일반 배송) - 3000원"
    else:
        print("택배(일반 배송) - 3000원")
# 무게가 2kg 미만이면
else:
    # 등기 선택 여부 입력받기 (Y/N)
    registration = input("등기 우편으로 하시겠습니까? (Y/N): ")
    # 등기이면 "우편(등기) - 2000원"
    if registration == "Y":
        print("우편(등기) - 2000원")
    # 등기가 아니면 "우편(일반) - 1000원"
    else:
        print("우편(일반) - 1000원")


