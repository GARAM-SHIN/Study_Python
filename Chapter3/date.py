# 날짜 / 시간 출력하기
import datetime

now =  datetime.datetime.now()    # 현재 날짜 / 시간을 구함

print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")