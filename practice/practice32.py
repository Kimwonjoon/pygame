# with
# import pickle
# # profile.pickle이라는파일을 읽기전용으로 불러오고 file의 정보를 profile_file 이라는 변수에 넣어줌
# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file)) # file의 정보를 갖고 있는 변수를 pickle.load를 이용해서 값을 가져와서 출력함
# # close 필요 없음

# with open("study.txt", "w", encoding="utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())