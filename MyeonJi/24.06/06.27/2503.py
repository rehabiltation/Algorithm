from itertools import permutations

# 입력 받기
N = int(input())

# 1부터 9까지의 숫자들로 구성된 모든 가능한 세 자리 수 생성
ans = [''.join(p) for p in permutations('123456789', 3)]

for _ in range(N):
    num, strike, ball = map(int, input().split())
    num = str(num)
    
    new_ans = []
    for a in ans:
        s, b = 0, 0
        for j in range(3):
            if a[j] == num[j]:
                s += 1
            elif num[j] in a:
                b += 1
                
        if s == strike and b == ball:
            new_ans.append(a)
    
    ans = new_ans

print(len(ans))
