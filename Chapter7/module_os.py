# os 모듈
import os

print("현재 운영체제:", os.name)    # 기본 정보 출력
print("현재 폴더:", os.getcwd())
print("현재 폴더 내부의 요소:", os.listdir())

os.mkdir("hello")    # 폴더를 만들고 제거하기 (폴더가 비어있을 때만 제거 가능)
os.rmdir("hello")

with open("original.txt", "w") as file:    # 파일을 생성하고 파일 이름 변경
    file.write("hello")
os.rename("original.txt", "new.txt")

os.remove("new.txt")    # 파일 제거하기
# os.unlink("new.txt")

os.system("dir")    # 시스템 명령어 실행