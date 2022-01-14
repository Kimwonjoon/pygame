# 다양한 출력 포맷
# 빈자리는 빈공간으로 두고, 우측 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))
# 양수일 땐 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))
# 좌측 정렬하고, 빈칸을 _로 채움
print("{0:_<10}".format(500))
# 3자리마다 콤마를 찍어주기 ex 1,000
print("{0:,}".format(100000000000))
# 3자리마다 콤마 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))
# 3자리 마다 콤마를 찍어주기, 부호도 붙이고, 자릿수도 확보하기
# 돈이 많으면 빈자리는 ^ 로 채워주기
print("{0:^<+30,}".format(10000000000000000000))
# 정리하자면 {0:빈자리,정렬,부호,자리수,3자리마다찍을거} 이순서로 넣어주면 됩니다. 실제로 적을땐 중간중간 , 없이 그냥 연속해서 적을것
# 소수점 출력
print("{0:f}".format(5/3))
# 소수점을 특정자리수까지만 표시하기 (소수점 셋쨰 자리에서 반올림)
print("{0:.2f}".format(5/3))