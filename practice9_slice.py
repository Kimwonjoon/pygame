#슬라이싱 = 원하는 정보만 잘라서 가져오기
jumin = "000507-1234567"

print("성별 :" +jumin[7]) # 컴퓨터는 첫자리를 0부터 셈
print("연 :" + jumin[0:2]) # [0:2] 0부터 2 직전까지
print("월 : " + jumin[2:4]) # 2부터 3까지
print("일 : " + jumin[4:6])

print("생년월일 : " + jumin[0:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6직전까지 처음부터 가져오는거면 굳이 0 필요 X
print("뒤 7자리 : " + jumin [7:14])
print("뒤 7자리 : " + jumin [7:]) # 7번째부터 끝까지
print("뒤 7자리 (뒤에부터) : " + jumin[-7:]) 
#맨뒤에서 7번째부터 끝까지 / 거꾸로 세는건 -1부터 시작
print(jumin[-6])