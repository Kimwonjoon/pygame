# 애완동물 소개해주세요 (주석 = 코드에는 포함되어있지만 실행할때는 무시되는 문장)
animal = "고양이"
name = "해피"
age = 6
hobby = "간식"
is_adult = age >= 7 # 나이가 7살 이상이면 어른

''' 이렇게
하면
여러문장이
주석처리
됩니다
'''

print("우리집 " + animal + "의 이름은 " + name + "에요")
hobby = "공놀이" #위에서부터 명령이 내려오니까 10번째 문장부터는 hobby가 공놀이임
#print(name + "는 "+ str(age) + "살이며, " + hobby + "을 아주 좋아해요") #숫자형 자료를 문자형 자료로 바꿔주는 str
print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요") #+ 대신 ,를 사용해도 정상적으로 출력 가능 대신 한칸씩 띄울것
print(name +"는 어른일까요? " + str(is_adult)) # is_adult가 숫자형자료라 문자형으로 바꿔줘야함