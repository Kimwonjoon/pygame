# 사전 dic
cabinet = {3:"유재석", 100:"김태호"} # 좌측이 key 값 오른쪽이 value 값
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3)) # get을 사용해서 value를 가져오면 소괄호 사용
# # print(cabinet[5]) # 이건 아예 오류나서 출력 종료
# print(cabinet.get(5)) # 이건 None으로 출력하고 다음것도 계속 출력함
# print(cabinet.get(5, "사용 가능")) 
# print("hi")

# 사전 자료형 안에 이 값이 있는지 확인
# print(3 in cabinet)
# print(5 in cabinet)

cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 새 손님 등장
print(cabinet)
cabinet["A-3"] = "김종국" # 유재석이 사용하던 키를 김종국이 사용하게 됨
cabinet["C-20"] = "조세호" # 조세호가 추가됨
print(cabinet)

# 손님 퇴장
del cabinet["A-3"]
print(cabinet)

# key 들만 출력
print(cabinet.keys())

# value 들만 출력
print(cabinet.values())

# 둘다 쌍으로 출력
print(cabinet.items())

# 목욕탕 폐점
cabinet.clear()
print(cabinet)