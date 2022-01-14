# 에러 발생 시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1= int(input("첫번째 숫자를 입력하세요 : "))
#     num2= int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
    
# 사용자 정의 예외 처리
class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기")
#     num1= int(input("첫번째 숫자를 입력하세요 : "))
#     num2= int(input("두번째 숫자를 입력하세요 : "))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
#     print(err)

# finally 에러가 발생하던지 문제가 생기던지 무조건 실행되는 구문 try문을 사용할때 맨 마지막에 넣어줌
try:
    print("한 자리 숫자 나누기 전용 계산기")
    num1= int(input("첫번째 숫자를 입력하세요 : "))
    num2= int(input("두번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
except ValueError:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
except BigNumberError as err:
    print("에러가 발생하였습니다. 한자리 숫자만 입력하세요.")
    print(err)
finally:
    print("계산기를 이용해 주셔서 감사합니다.")