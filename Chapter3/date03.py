# 계절을 구분하는 프로그램
import datetime

now = datetime.datetime.now()

if 3 <= now.month <= 5:    # 봄 구분
    print("이번 달은 {}월로 봄입니다!".format(now.month))

if 6 <= now.month <= 8:    # 여름 구분
    print("이번 달은 {}월로 여름입니다!".format(now.month))

if 9 <= now.month <= 11:    # 가을 구분
    print("이번 달은 {}월로 가을입니다!".format(now.month))

if now.month == 12 or 1 <= now.month <= 2:    # 겨울 구분
    print("이번 달은 {}월로 겨울입니다!".format(now.month))