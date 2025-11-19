# 숫자로 변환되는 것들만 리스트에 넣기
list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
    try:
        float(item)    # 예외가 발생하면 알아서 다음으로 진행되지 않겠지?
        list_number.append(item)    # 예외 없이 대상이 통과되었으면 list_number 리스트에 넣어줘
    except:
        pass

print("{} 내부에 있는 숫자는".format(list_number))
print("{}입니다.".format(list_number))