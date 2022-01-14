# 가변인자 *
# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

def profile(name, age, *language):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ") # end = " "를 사용해주면 아래에 있는 함수도 한줄로 같이 호출됩니다.
    for lang in language:
        print(lang, end=" ")
    print()

profile("유재석", 20, "Python", "Java", "C", "C++", "C#", "JavaScript")
profile("김태호", 25, "Kotlin", "Swift")
# 유재석이 할 수 있는 언어가 늘어나면 함수자체를 바꿔줘야하는데 이런걸 위해 가변인자가 존재함
# 가변인자를 사용해주면 위처럼 귀찮게 하지 않아도 됨