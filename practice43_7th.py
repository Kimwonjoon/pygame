# 예외 처리
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0] / nums[1]))
    print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
except ValueError: # try 내부에서 발생하는 오류에 해당하는 오류가 발생하면 아래의 문장을 print함
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err: # Value 에러, 제로디비전에러가 아닌 다른 모든 에러에 대해서 이렇게 처리가 가능함
    print("알 수 없는 에러가 발생하였습니다.")
    print(err)