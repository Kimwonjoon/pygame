# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) # 문장을 소문자로 출력
print(python.upper()) # 문장을 대문자로 출력
print(python[0].isupper()) # 몇번째 단어가 대문자가 맞는지 질문
print(len(python)) # 함수 문장의 길이를 알려줌
print(python.replace("Python", "Java")) # 원하는 곳을 다른 문자열로 바꿔줌

index = python.index("n") # n이라는 글자의 위치를 찾아줌
print(index)
index = python.index("n", index + 1) # 두번째 n의 위치를 찾아줌
print(index)

# find 와 index의 차이점
print(python.find("Java")) # 원하는 값이 변수에 포함되어있지 않으면 -1 출력
# print(python.index("Java")) # 원하는 값이 없으면 오류를 내버림
# index 와 find 의 기능은 같지만 index를 사용했을때 원하는 값이 없으면 오류를 내버리니까 index줄
# 아래의 문장들이 작동을 못하게함
print("hi")

print(python.count("n")) # 내가 원하는 값이 몇번 등장하는지 알려줌