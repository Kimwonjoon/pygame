from random import *

offline = int((random() * 28) + 4) # 4일 ~ 28일 중 랜덤 택 1

print("오프라인 스터디 모임 날짜는 매월", offline, "일로 선정되었습니다.")
print("오프라인 스터디 모임 날짜는 매월"+ str(offline) +"일로 선정되었습니다.")
# + 를 사용할때는 offline이 정수형 자료니까 str 사용해서 문자형으로 변환 시켜줘야 출력이 됨

offline = randrange(4, 29) # 4일 ~ 29일 미만

print("오프라인 스터디 모임 날짜는 매월", offline, "일로 선정되었습니다.")

offline = randint(4,28) # 4일 ~ 28일 이내

print("오프라인 스터디 모임 날짜는 매월", offline, "일로 선정되었습니다.")