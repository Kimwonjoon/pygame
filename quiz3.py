#내 풀이
# url = "http://naver.com"
# a = url[7:12]
# print(a)

# b = a[0:3]
# c = len(a)
# d = a.count('e')
# e = "!"
# print(str(b)+str(c)+str(d)+e)

# 정답
url = "http://naver.com"
my_str = url.replace("http://", "")
# print(my_str)
my_str = my_str[:my_str.index(".")] # = my_str[0:5]
# print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# 정수를 문자와 합치고 싶으면 str을 적어서 정수형을 문자형자료로 전환시켜주면 된다.
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password))