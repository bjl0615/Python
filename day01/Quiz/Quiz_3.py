# Quiz) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.coom
# 규칙 1 : http:// 부분은 제외 => naver
# 규칙 2 :처음 만나는 점 (.) 이후 부분은 제외 => naver 
# 규칙 3 : 남은 글자 중 처음 세자리 + 글자 갯수 _ 글자 내 'e' 갯수 + "!"  로구성
#                     (nav)           (5)             (1)         (!)

# 예) 생성된 비밀번호 : nav51!

url = "http://daum.net"
my_str = url.replace("http://", "") # http://를 공백으로 변경
my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0 ~ 5 직전까지. (0, 1, 2, 3, 4)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!" # my_str의 0부터 2번쨰 자리까지 + my_str의 길이 + my_str의 e의 갯수
print("{0} 의 비밀번호는 {1} 입니다.".format(url , password)) 

