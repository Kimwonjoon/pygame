# 파일 입출력
# score_file = open("score.txt", "w", encoding="utf8") # w = 쓰기용도
# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8") # 계속 이어서 내용을 쓰고 싶으면 a(append)
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100") # print에선 자동으로 줄바꿈이 되지만 여기에선 줄바꿈을 해줘야함 이렇게 사용할땐
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.readline(), end="") # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# print(score_file.readline(), end="")
# score_file.close()

# 몇줄인지 모를때 어떻게 읽어올까?
# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end="")
# score_file.close()

# 리스트에 값을 넣어서 처리도 가능
score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines() # readlines 는 파일에 있는 모든 문장을 읽음 이 문장은 lines에 리스트 형태로 파일에 있는걸 집어넣음
for line in lines:
    print(line, end="")

score_file.close()