#함수
def open_account(): # 함수는 호출하기 전까지는 실행이 되지않음
    print("새로운 계좌가 생성되었습니다.")

# open_account() # 이렇게 호출해주면 터미널에 실행 됨

# 전달값과 반환값

def deposit(balance, money): # 입금
    print("입금이 완료 되었습니다. 잔액은 {0} 원입니다.".format(balance + money))
    return balance + money # 반환하려면 return 사용 
    # 반환 되어서 balance + money 값이 balance로 들어감

def withdraw(balance, money): # 출금
    if balance >= money: # 잔액이 출금액보다 많으면 출금 가능
        print("출금이 완료되었습니다. 잔액은 {0} 원입니다.".format(balance - money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0} 원입니다.".format(balance))
        return balance

def withdraw_night(balance, money): # 저녁에 출금 수수료 증가
    commission = 100 # 수수료 100원
    return commission, balance - money - commission # 두개의 값을 튜플 형식으로 보내주기

balance = 0 # 잔액
balance = deposit(balance, 1000) # 이게 def 뒤에 있는곳으로 이동
# balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500)
commission, balance = withdraw_night(balance, 500)
print("수수료 {0} 원이며, 잔액은 {1} 원입니다.".format(commission, balance))
print(balance) # 반환이 완료된 balance 를 출력하면 1000 원이 나옴