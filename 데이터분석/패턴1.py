import re

pattern = r"^abc"
# pattern = r"abc"
# pattern = r"abc$"
# pattern = r"[p|P]ython"
# r" " 쌍따옴표 안에 대괄호를 넣으면, 대괄호 안에 있는것은 제외하라는 의미
# python인데, p는 대소문자 구분하지 말고 ython 인 경우를  찾기 위함임

text = ["abc", "abcd", "abc15", "dabc", "", "s", "I love kabcde"]
repattern = re.compile(pattern)

for item in text:
    result = repattern.search(item)
    if result:
        print(item, "- O" )
    else:
        print(item, "- X" )

