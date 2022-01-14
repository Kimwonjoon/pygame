# 클래스
# 마린 : 공격 유닛, 군인. 총을 쏠 수 있음
# name = "마린" # 유닛 이름
# hp = 40 # 유닛 체력
# damage = 5 # 유닛 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력 {1}\n".format(hp, damage))

# # 탱크 : 공격 유닛, 탱크. 포를 쏠 수 있는데, 일반 모드가 있고 시즈모드가 있음.
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank_name))
# print("체력 {0}, 공격력 {1}\n".format(tank_hp, tank_damage))
# # 이렇게 복사해서 유닛을 더 만들기엔 게임에 유닛이 몇백마리라 힘드니까 클래스를 사용해서 편하게 만들기
# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{} 유닛이 생성되었습니다.".format(tank2_name))
# print("체력 {0}, 공격력 {1}\n".format(tank2_hp, tank2_damage))

# def attack(name, loccation, damage):
#     print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(name, loccation, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)
# 클래스 = 붕어빵 틀이라고 생각하면 쉬움

class Unit:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
# unit에 의해서 생성되는 아래 마린, 탱크는 객체
# __init__ 안에 있는 맨앞줄 self 제외한 다른 값들의 개수만큼 값을 넘겨줘야함.
marine1 = Unit("마린", 40, 5)
marine2 = Unit("마린", 40, 5)
tank = Unit("탱크", 150, 35)

# __init__ = 파이썬에서 사용하는 생성자, 위의 마린이나 탱크 같은 객체들이 만들어질때 자동으로 호출되는 부분