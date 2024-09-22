import sys
from itertools import combinations

# 입력 받기
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 집과 치킨집의 위치 리스트
home = []
chicken = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            home.append((i, j))
        elif arr[i][j] == 2:
            chicken.append((i, j))

# 치킨 거리 계산 함수
def cal(seleted_chicken):
    total = 0
    for hy, hx in home:
        min_dist = float('inf')
        for cy, cx in seleted_chicken:
            min_dist = min(min_dist, abs(hy - cy) + abs(hx - cx))
        total += min_dist
    return total

# 치킨집 M개 선택하기
def dfs(idx, selected):
    global ans
    # M개 다 선택했을 때
    if len(selected) == M:
        ans = min(ans, cal(selected))
        return
    # 모두 탐색했을 때
    if idx >= len(chicken):
        return
    # 현재 치킨집 선택했을 때
    dfs(idx+1, selected+[chicken[idx]])
    # 현재 치킨집을 선택 안할 때
    dfs(idx+1, selected)

ans = int(1e9) # 최소 거리 저장할 변수
dfs(0, []) # 탐색 시작하깅
print(ans)