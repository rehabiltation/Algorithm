# 문제

"""
알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
"""

# 입력

# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력

# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 풀이

word = input()
word = list(word.upper())

comp_dict = {}
while word:
    a = word.pop()
    if a in comp_dict:
        comp_dict[a] += 1
    else:
        comp_dict[a] = 1

max_val = max(comp_dict.values())
max_keys = []

for key, value in comp_dict.items():
    if value == max_val:
        max_keys.append(key)


if len(max_keys) == 1:
    print(*max_keys)
else:
    print("?")