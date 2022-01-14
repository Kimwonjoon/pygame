# 튜플 리스트보다 속도는 빠르지만 목록 수정이 안됨
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") # 오류뜸

# name = "김종국"
# age = 20
# hobby = "코딩"
# print(name, age, hobby)

# 위에껄 튜플 활용

(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby)