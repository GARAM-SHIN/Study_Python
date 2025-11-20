# urllib 모듈
from urllib import request    # 모듈을 읽어 들임

target = request.urlopen("https://google.com")    # urlopen() 함수로 구글의 메인 페이지를 읽음
output = target.read()

print(output)