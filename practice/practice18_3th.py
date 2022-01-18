# if문
weather = input("오늘 날씨는 어때요? ") # input 사용하면 우측 터미널에 입력을 기다림
if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else: # 위에 조건들이 다 안맞으면 else 출력
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요? ")) # 입력하는게 위와는 달리 정수형을 입력해줘야해서 int로 감싸줌
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")