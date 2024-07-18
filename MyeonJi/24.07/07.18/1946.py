import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    score = [list(map(int, input().split())) for _ in range(N)]
    score_list = sorted(score)

    top = 0
    result = 1

    for i in range(1, len(score_list)):
        if score_list[i][1] < score_list[top][1]:
            top = i
            result += 1

    print(result)