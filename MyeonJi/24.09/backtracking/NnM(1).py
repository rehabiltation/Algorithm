import sys
input = sys.stdin.readline

def solution(N, M):
    used = [False] * (N+1)
    backtrack(N, M, [], used)

def backtrack(N, M, seq, used):
    if len(seq) == M:
        print(' '.join(map(str, seq)))
        return

    for i in range(1, N+1):
        if not used[i]:
            used[i] = True
            seq.append(i)
            backtrack(N, M, seq, used)
            seq.pop()
            used[i] = False

N, M = map(int, input().split())
solution(N, M)

'''
def backtracking(num):
    if num == M:
        print(*path)
        return
    for i in num_list:
        if i in path:
            continue
        path[num] = i
        backtracking(num+1)
        path[num] = 0

N, M = map(int, input().split())
num_list = [i for i in range(N+1)]
path = [0] * M
backtracking(0)
'''