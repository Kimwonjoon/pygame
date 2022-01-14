# 반복문 for
# print("대기번호 : 1")
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

# for waiting_no in [0,1,2,3,4]: # 뒤의 리스트내에서 좌측부터 입력되면서 출력
#     print("대기번호 : {0}".format(waiting_no))

# for waiting_no in range(1, 6): # 1 ~ 5까지
#     print("대기번호 : {0}".format(waiting_no))

starbucks = ["아이언맨", "토르", " 그루트"]
for customer in starbucks:
    print("{0}, 커피가 준비되었습니다.".format(customer))