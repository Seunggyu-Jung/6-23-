url = "http://naver.com"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
passward = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{}의 비밀번호는 {}입니다.".format(url,passward))

url = "http://daum.net"
my_str = url.replace("http://","")
my_str = my_str[:my_str.index(".")]
passward = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{}의 비밀번호는 {}입니다.".format(url,passward))