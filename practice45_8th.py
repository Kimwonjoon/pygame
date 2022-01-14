# 모듈 : 같은 폴더에 모듈이 있어야 사용이 가능함
# import theater_module
# theater_module.price(3) # 3명이서 영화 보러 갔을 때 가격
# theater_module.price_morning(4) # 4명이서 조조 할인 영화 보러 갔을 때
# theater_module.price_soldier(5) # 5명의 군인이 영화 보러 갔을 때

# import theater_module as mv # theater_module 을 쓰기엔 귀찮으니까 별명을 붙여주는것
# mv.price(3)
# mv.price_soldier(3)
# mv.price_morning(3)

# from theater_module import * # 이거는 앞에 모듈의 이름을 안적어줘도 출력이 가능함
# # from random import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning # 원하는 부분만 가져올 수 있음
# price(5)
# price_morning(6)

from theater_module import price_soldier as price # price_soldier에 price 라는 별명을 붙여줬음
price(4)