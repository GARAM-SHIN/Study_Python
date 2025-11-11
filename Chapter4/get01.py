# 키가 존재하지 않을 때 None을 출력하는지 확인하기
dictionary = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

value = dictionary.get("존재하지 않는 키")    # 존재하지 않는 키에 접근하기
print("값:", value)

if value == None:    # None 확인 방법
    print("존재하지 않는 키에 접근했었습니다.")