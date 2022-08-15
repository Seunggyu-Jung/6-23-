# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오
# 
# 예) http://naver.com, daum, google
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 내 'e' 갯수 + "!"로 구성
# 예)  nav51!



url = "http://naver.com"
 
print(url[7:]) #규칙1

url2 = url[7:]

print(url2[0:5]) #규칙2

url3 = url2[0:5]
url5 = url3[0:3]
url4 = url3.count("e")
print(url5, url4, "!")


