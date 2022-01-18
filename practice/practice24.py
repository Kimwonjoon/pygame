# 기본값 설정

# def profile(name, age, main_lang):
#     print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
#         .format(name, age, main_lang)) # 줄바꿈
# \t = tab 한번 누른것처럼 띄어쓰기 후 출력
# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

# 같은 학교 같은 학년 같은 반 같은 수업

def profile(name, age = 17, main_lang = "파이썬"):
    print("이름 : {0}\t나이 : {1}\t주 사용 언어: {2}"\
        .format(name, age, main_lang))

profile("유재석", 20)
profile("김태호")
# 따로 호출되지 않으면 입력 되어있는 17살, 파이썬이 기본으로 출력 됨
# 값을 넣으면 넣은 값으로 수정되어서 출력이 됩니다.