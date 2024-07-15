# 문제

"""
은민이는 4와 7을 좋아하고, 나머지 숫자는 싫어한다. 금민수는 어떤 수가 4와 7로만 이루어진 수를 말한다.

A와 B가 주어졌을 때, A보다 크거나 같고, B보다 작거나 같은 자연수 중에 금민수인 것의 개수를 출력하는 프로그램을 작성하시오.
"""

# 입력

# 첫째 줄에 A와 B가 주어진다. A는 1보다 크거나 같고, 1,000,000,000보다 작거나 같은 자연수이다. B는 A보다 크거나 같고, 1,000,000,000보다 작거나 같은 자연수이다.

# 출력

# 첫째 줄에 A보다 크거나 같고, B보다 작거나 같은 자연수 중에 금민수인 것의 개수를 출력한다.

# 정답

from itertools import product

a, b = map(int, input().split())
a_len = len(str(a))
b_len = len(str(b))
count = 0
for i in range(a_len, b_len + 1):
    for n in product([4, 7], repeat=i):
        join = ''.join(list(map(str, n)))
        if a <= int(join) <= b:
            count += 1
print(count)