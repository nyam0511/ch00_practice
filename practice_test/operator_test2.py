# 이름과 메시지를 입력받기

# 이름 입력받기
name = input("이름: ")

# 메시지 입력받기 (세상에 공짜는 없다!)
message = input("메시지: ")

# * 20개 출력
print("*" * 20)
# * 이름 님의 한마디 * 출력
print(f"* {name} 님의 한마디 *")
# print("*" + name + " 님의 한마디")
#print("*", name, "님의 한마디", "*")
# * 메시지 * 출력
#print(f"* {message} *")
#print("* " + message + " *")
print("*", message, "*")
# * 20개 출력
print("*" * 20)