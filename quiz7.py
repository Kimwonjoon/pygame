# 실행 시키면 txt 파일 50개 만들어지니 주의
for i in range(1,51):
    with open("{0}주차.txt".format(i), "w", encoding="utf8") as bogo:
        bogo.write("- {0} 주차 주간보고 -".format(i))
        bogo.write("\n부서 : ")
        bogo.write("\n이름 : ")
        bogo.write("\n업무 요약 : ")

# 유투부 정답 방식
for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as bogo: # X 주차 입력 방식만 다름
        bogo.write("- {0} 주차 주간보고 -".format(i))
        bogo.write("\n부서 : ")
        bogo.write("\n이름 : ")
        bogo.write("\n업무 요약 : ")