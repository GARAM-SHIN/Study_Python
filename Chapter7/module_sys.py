# sys 모듈
import sys

print(sys.argv)    # 명령 매개변수를 출력함
print("---")

print("getwindowvesrsion:()", sys.getwindowsversion())    # 컴퓨터 환경과 관련된 정보를 출력함
print("---")
print("copyright:", sys.copyright)
print("---")
print("version:", sys.version)

sys.exit()    # 프로그램을 강제로 종료함