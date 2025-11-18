# 가변 매개변수 함수
def print_n_times(n, *values):
    for i in range(n):    # n번 반복함
        for value in values:    # values는 리스트처럼 활용함
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")