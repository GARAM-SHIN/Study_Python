# 파일 처리 중간에 예외 발생
try:
    file = open("info.txt", "w")
    예외.발생해라()    # 일부러 예외 발생하기
    file.close()
except:
    print("오류가 발생했습니다.")

print("# 파일이 제대로 닫혔는지 확인하기")
print("file.closed:", file.closed)