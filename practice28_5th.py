# 표준 입출력
# print("Python", "Java", "JavaScript", sep=",", end = "?") # sep를 사용해서 띄어쓰기를 할지 중간중간에 뭘 넣을지 정할수 있음
# print("무엇이 더 재밌을까요?") # end = "?" 를 이용해서 위 문장의 끝부분에 ?를 추가하면서 아래의 문장을 이어서 나오도록 함

# import sys
# print("Python", "Java", file = sys.stdout) # stdout = 표준 출력으로 처리
# print("Python", "Java", file = sys.stderr) # stderr = 표준 에러로 처리

#시험성적
# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): # 딕셔너리에 있는 key, value 값을 subject, score에 튜플형식으로 보내줌
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":") # ljust(8) = 왼쪽으로 정렬을 하는데 8칸의 공간을 확보한다., rjust는 우측정렬

# 은행 대기 순번표
# ex) 001, 002, 003, ...
# for num in range(1,21):
#     print("대기번호 : " + str(num).zfill(3)) # zfill(3) = 3칸만큼의 공간을 확보하며 빈칸은 0으로 채워라

answer = input("아무 값이나 입력하세요 : ") # 아래 터미널에 값을 입력하면 입력한 값이 answer로 들어가면서 answer 값이 변하는거임
print(type(answer)) # 사용자 입력 형태면 무조건 str 형태로 나옴
print("입력하신 값은 " + answer + "입니다.") # 그래서 여기에서 answer을 str로 안감싸줘도 에러가 안뜸