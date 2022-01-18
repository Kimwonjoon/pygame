#continue, break 반복문 내에서 사용 가능
absent = [2, 5] # 결석
no_book = [7] # 책을 깜빡했음
for student in range (1, 11): # 1~10번까지 출석번호가 있음
    if student in absent:
        continue # 아래에 있는 문장을 더 실행시키지말고 다시 반복을 시켜라 = 2, 5번 차례엔 아래의 print 책을 읽어봐 문장이 출력이 안됨
    elif student in no_book:
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break # 뒤에 반복문이 있던없던 그냥 문장 끝내버림
    print("{0}. 책을 읽어봐".format(student))