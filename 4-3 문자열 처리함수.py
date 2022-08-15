python = "Python is Amazing."
print( python.lower()) # 소문자로 출력 : .lower()
print(python.upper())  # 대문자로 출력 : .upper()
print(python[0].isupper()) # 0번째 문자가 대문자인가? : [].isupper
print(len(python)) # 문자열의 길이 : len()
print(python.replace("Python","Java")) # .replace("이전 것","바꿀 것")


index = python.index("n") # .index("") : 몇번째 문자열인가? * 해당문자가 없을 경우, 오류로 코딩 종료 
print(index)
index = python.index("n", index + 1) # .index("") , index + n : 다음문자가 몇번째 문자열인가?
print(index)

print(python.find("n")) # .find("") : 몇번째 문자열인가? * 해당 문자가 없을 경우, -1 값 출력
print(python.index("n"))  

print(python.count("n")) # .count("") : 해당 문자가 몇번나오는가?