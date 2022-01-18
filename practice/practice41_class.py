class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() # 다중 상속 코드를 작성 했을때, super()를 사용하면 순서상 맨 처음 클래스에 대해서 __init__ 함수가 호출됨
        # 다중 상속을 할때, 모든 부모 클래스의 생성자를 호출하려면 각 부모 클래스의 이름을 통해서 접근할 것
        Unit.__init__(self)
        Flyable.__init__(self)

# 드랍쉽
dropship = FlyableUnit()

# 다중 상속을 받을땐 super를 사용해서 한방에 초기화 하지말고 각각 상속받는 클래스 나눠서 초기화 시켜야함