from random import *

print(random()) # 0.0 ~ 1.0 미만의 임의의 값 생성
print(random() * 10) # 0.0 ~ 10.0 미만의 임의의 값 생성
print(int(random() * 10)) # 실수를 정수로 출력
print(int(random() * 10)) # 소수점 안보이게 출력
print(int(random() * 10)) # 소수점 안보이게 출력
print(int(random() * 10) + 1) # 1 ~ 10 이하의 임의의 값 생성

print(int(random() * 45) + 1) # 1 ~ 45 이하의 임의의 값 생성 로또 번호

print(randrange(1, 46)) # 1~ 46 미만의 임의의 값 생성

print(randint(1 ,45)) # 1 ~ 45 이하의 임의의 값 생성