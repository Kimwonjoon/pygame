# 패키지 = 모듈들을 모아놓은 집합체
# import travel.thailand # 클래스나 함수는 직접 import가 불가능함 패키지나 모듈만 가능
# import travel.thailand.ThailandPackage # 클래스를 직접 가져오는건 불가능
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel.thailand import ThailandPackage # from을 사용하면 클래스를 바로 가져올수있음
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# __all__ 함수
from travel import * # 이렇게 * 을 사용해서 travel에 있는걸 모두 가져오려고 할땐 공개 범위를 설정해줘야 사용이 가능함
# travel 폴더의 __init__에서 __all__ = ["thailand"] 와 같이 공개 범위를 설정해줘야 오류 없이 패키지, 모듈을 가져와서 사용할수있음
# trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

# 패키지, 모듈 위치 확인
import inspect
import random
print(inspect.getfile(random))
print(inspect.getfile(thailand))