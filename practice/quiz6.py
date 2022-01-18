# def std_weight(height, gender):
#     if gender == "남자":
#         std_weight = height** 2 * 22
#         print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다".format(height*100, round(std_weight, 2)))
#     else:
#         std_weight = height** 2 * 21
#         print("키 {0}cm 여자의 표준 체중은 {1}kg 입니다".format(height*100, round(std_weight, 2)))

# std_weight = std_weight(1.75, "남자")

# 풀이

# def std_weight(height, gender): # 키 m 단위 (실수), 성별 "남자" / "여자"
#     if gender == "남자":
#         return height ** 2 * 22
#     else:
#         return height ** 2 * 21

# height = 175 # cm 단위
# gender = "남자"
# weight = round(std_weight(height / 100, gender), 2) # 소수점 두번째 자리까지만 출력하는것 round(a, 2)
# print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))

def std_weight (sex, height):
    if sex == "male":
        # print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, round(height / 100 * height / 100 * 22, 2)))
        print("키 {0}cm 남자의 표준 체중은 {1}kg 입니다.".format(height, height / 100 * height / 100 * 22))
        # height에서 받은 175 가지고 그냥 출력을 때렸으니까 round 없이 그냥 67.375kg 나온거고
        return height ** 2 * 22
    else:
        print("키 {0}*100 여자의 표준 체중은 {1}kg 입니다.".format(height, height / 100 * height / 100 * 21))
        return height ** 2 * 21
weight = round(std_weight("male", 175), 2) # 이건 그냥 return 받은 값이라 673750 나오는거고
print(weight)