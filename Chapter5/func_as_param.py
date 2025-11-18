# 함수의 매개변수로 함수 전달하기
def call_10_times(func):    # 매개변수로 받은 함수를 10번 호출하는 함수
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요")

call_10_times(print_hello)