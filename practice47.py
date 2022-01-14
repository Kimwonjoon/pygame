# pip로 패키지 설치하기 = 다른 사람이 만든거 다운로드
from bs4 import BeautifulSoup
soup = BeautifulSoup("<p>some<b>bad<i>HTML")
print(soup.prettify())