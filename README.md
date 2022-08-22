# 나도코딩 파이썬: 4강 문자열

## 1. 문자열

- 변수를 만들어서 print로 출력한다. `sentence = '나는 소년입니다.' -> print(sentence)`
- 문자는 작은 따옴표든 큰 따옴표든 상관없다.

## 2. 슬라이싱

-  슬라이싱 : 문자열에서 필요한 부분만 짤라서 쓰는 것
```
jumin = "970927-1234567"
print( "성별 : " + jumin[7]) -> 성별 : 1
print(" 연 : " + jumin[0:2]) # [0:2] : 0부터 2 직전까지 -> 연 : 97
print( "월 : " + jumin[2:4]) -> 월 : 09
print("일 : " + jumin[4:6]) -> 일 : 27

print("생년월일 : " + jumin[:6]) # 처음부터 6 직전까지 -> 생년월일 : 970927
print("뒤 7자리 : " + jumin[7:]) # 7부터 끝까지 -> 뒤 7자리 : 1234567
print("뒤 7자리 (뒤서부터) : " + jumin[-7:]) -> 뒤 7자리 (뒤서부터) : 1234567
```

## 3. 문자열 처리함수
`python = "Python is Amazing."`
- .lower() : 소문자로 출력 , `print( python.lower()) -> python is amazing.`
- .upper() : 대문자로 출력, `print(python.upper()) -> PYTHON IS AMAZING.`
- [].isupper() : []번째 문자가 대문자인가?, `print(python[0].isupper()) -> True`
- len() : 문자열의 길이, `print(len(python)) -> 18`
- .replace("이전 것","바꿀 것") : 문자열을 바꾸는 것, `print(python.replace("Python","Java")) -> Java is Amazing.`
- .index("") : 몇번째 문자열인가? 없을 경우 코딩 종료, `index = python.index("n") , print(index) -> 5`
- .index("", index + n) : 다음문자가 몇번째 오는가?, `index = python.index("n", index + 1) , print(index) -> 15`
- .find("") : 몇번째 문자열인가? 해당 문자가 없을 경우, -1 값 출력, `print(python.find("n")) ->5 `
- .count("") : 해당 문자가 몇번나오는가?, `print(python.count("n")) -> 2`