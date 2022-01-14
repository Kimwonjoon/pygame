# 멤버변수
class Unit:
    def __init__(self, name, hp, damage):
        # 아래 세줄이 멤버 변수
        self.name = name
        self.hp = hp
        self.damage = damage
        print("{0} 유닛이 생성 되었습니다.".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스 : 공중 유닛, 비행기. 클로킹 (상대방에게 보이지 않음)
wraith1 = Unit("레이스", 80, 5)
print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# 마인드 컨트롤 : 상대방 유닛을 내 것으로 ㅁ나드는 것 (빼앗음)
wraith2 = Unit("빼앗은 레이스", 80, 5)
wraith2.clocking = True
# 클래스 외부에서 확장해서 적용할수있음

if wraith2.clocking == True: # wraith1 에는 클로킹이 없음
    print("{0} 는 현재 클로킹 상태입니다.".format(wraith2.name))
