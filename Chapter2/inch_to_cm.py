# inch 단위를 cm 단위로 변경하기
raw_input = input("inch 단위의 숫자를 입력해주세요: ")    # 숫자 입력받기

inch = int(raw_input)    # 입력받은 데이터를 숫자 자료형응로 변환하고  cm 단위로 변경하기
cm = inch * 2.54

print(inch, "inch는 cm 단위로", cm, "cm입니다.")