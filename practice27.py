#지역변수(함수내에서만 사용할 수 있는것), 전역변수(모든 공간에서 부를 수 있는 변수)
# 지역변수 예제
gun = 10 # 함수 밖에서의 gun 은 10정

# def checkpoint(soldiers): # 경계근무
#     gun = 20 # 안에서 정해주면 오류없이 돌아감 함수 안에서의 gun은 20정
#     gun = gun - soldiers # 안에 있는 gun은 값이 정해진게 없음
#     print("[함수 내] 남은 총 : {0}".format(gun)) # 함수안에서 남은 총은 18정

# print("전체 총 : {0}".format(gun)) # 함수 밖에서 전체 총은 10정
# checkpoint(2) # 2명이 경계 근무 나감
# print("남은 총 : {0}".format(gun)) # 함수 밖에서 남은 총도 10정

# 전역변수 예제
def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용 = 10
    gun = gun - soldiers 
    print("[함수 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers): # 전역변수 사용하는 것보단 이렇게 return 사용해서 계산해주는걸 추천함
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
# checkpoint(2) 
gun = checkpoint_ret(gun,2)
print("남은 총 : {0}".format(gun)) 