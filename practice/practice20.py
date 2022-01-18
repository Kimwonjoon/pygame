# 또다른 반복문 while 조건이 만족할때까지 반복하라는 것
# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비되었습니다. {1} 번 남았어요".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")

# customer = "아이언맨"
# index = 1
# while True :
#     print("{0}, 커피가 준비되었습니다. 호출 {1} 회".format(customer, index))
#     index += 1
# 이대로 출력하면 무한반복

customer = "토르"
person = "Unknown"
# person 이 내가 원하는 customer 가 아닐때까지 계속 반복해라 라는 뜻
while person != customer : # 적혀있는 조건에 만족할때까지 계속 반복
    print("{0}, 커피가 준비 되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요? ") # 여기에서 토르를 input 하면 person 과 customer 값이 같아지니까 더이상 반복을 하지 않는다.