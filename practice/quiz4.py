from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

users = range(1,21) # 1~20까지 숫자 생성
# print(type(users))
users = list(users)
# print(type(users))

# print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 4명중 1명 치킨, 3명 커피
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print("-- 축하합니다 --")