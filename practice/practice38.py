# 연산자 오버로딩 = 자식 클래스에서 정의한 메소드를 사용하고 싶을때 메소드를 새로 초기화하는 것
#일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
# 공격 유닛
class AttackUnit(Unit): # Unit 클래스의 정보를 상속받음
     def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed) # Unit 클래스의 name, hp 정보를 상속받았음. self.name = name, self.hp = hp 이런 함수를 물려받은것
        self.damage = damage

     def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name, location, self.damage))

     def damaged(self, damage):
         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
         self.hp -= damage
         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
         if self.hp <= 0:
             print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린 / 파이어뱃 / 탱크 등을 수송. 공격 X

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))
# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable): # 클래스 2개를 상속받아서 초기화
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage)
        Flyable.__init__(self, flying_speed)

    def move(self, location): # 새롭게 공중유닛 클래스에서 재정의를 해서 공중유닛이 move를 호출하면 여기에서 호출됨
        print("[공중 유닛 이동]")
        self.fly(self.name, location)

# 벌쳐 : 지상 유닛, 기동성 좋음
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루저 : 공중 유닛, 체력 굉장히 좋음, 공격력 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name, "9시")
# 연산자 오버로딩을 사용해서 알아서 지상유닛이면 이동하고 공중 유닛이면 날아갈수있도록 코딩
battlecruiser.move("9시")
