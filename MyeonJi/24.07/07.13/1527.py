# 금민수 은민수 동민수
# 브루트포스

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

'''
시간초과 ㅎ
A, B = map(int, input().split())
cnt = 0

for i in range(A, B + 1):
    if all(c == '4' or c == '7' for c in str(i)):
        cnt += 1

print(cnt)
'''