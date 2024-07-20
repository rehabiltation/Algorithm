from math import ceil
N = int(input())
arr = list(map(int,input().split()))
T, P = map(int, input().split())

t_ans = 0

for i in arr:
    a = ceil(i/T)
    t_ans += a

p_ans1 = N//P
p_ans2 = N%P

print(t_ans)
print(p_ans1, p_ans2)