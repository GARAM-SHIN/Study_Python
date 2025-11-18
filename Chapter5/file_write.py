# 랜덤하게 1000명의 키와 몸무게 만들기
import random

hanguls = list("가나다라마바사아자차카타파하")    # 간단한 한글 리스트 만들기

with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)    # 랜덤한 값으로 변수 생성
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)

        file.write("{}, {}, {}\n".format(name, weight, height))