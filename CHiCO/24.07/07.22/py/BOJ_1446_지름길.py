# 문제

"""
매일 아침, 세준이는 학교에 가기 위해서 차를 타고 D킬로미터 길이의 고속도로를 지난다. 이 고속도로는 심각하게 커브가 많아서 정말 운전하기도 힘들다. 어느 날, 세준이는 이 고속도로에 지름길이 존재한다는 것을 알게 되었다. 모든 지름길은 일방통행이고, 고속도로를 역주행할 수는 없다.

세준이가 운전해야 하는 거리의 최솟값을 출력하시오.
"""

# 입력

# 첫째 줄에 지름길의 개수 N과 고속도로의 길이 D가 주어진다. N은 12 이하인 양의 정수이고, D는 10,000보다 작거나 같은 자연수이다. 다음 N개의 줄에 지름길의 시작 위치, 도착 위치, 지름길의 길이가 주어진다. 모든 위치와 길이는 10,000보다 작거나 같은 음이 아닌 정수이다. 지름길의 시작 위치는 도착 위치보다 작다.

# 출력

# 세준이가 운전해야하는 거리의 최솟값을 출력하시오.

# 정답

# 모르겠다
# 입력 처리
n, d = map(int, input().split())
shortcuts = [tuple(map(int, input().split())) for _ in range(n)]

# DP 배열 초기화
dp = [float('inf')] * (d + 1)
dp[0] = 0

# 지름길 정보를 딕셔너리로 변환
shortcut_map = {}
for start, end, length in shortcuts:
    if end <= d:
        if start in shortcut_map:
            shortcut_map[start].append((end, length))
        else:
            shortcut_map[start] = [(end, length)]

# DP 배열 갱신
for i in range(d + 1):
    # 다음 지점으로 이동하는 경우
    if i + 1 <= d:
        dp[i + 1] = min(dp[i + 1], dp[i] + 1)
    
    # 지름길을 사용하는 경우
    if i in shortcut_map:
        for end, length in shortcut_map[i]:
            dp[end] = min(dp[end], dp[i] + length)

# 최종 결과 출력
print(dp[d])


# 다익스트라란?

# 다익스트라의 기본 구조
import heapq

def dijkstra(graph, start):
    # 시작 노드에서 각 노드까지의 최단 거리 테이블
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # 우선순위 큐를 생성하고 시작 노드를 추가
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # 현재 노드의 최단 거리가 이미 처리된 경우 무시
        if current_distance > distances[current_node]:
            continue
        
        # 현재 노드와 연결된 이웃 노드를 탐색
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            
            # 발견한 최단 거리가 기존 최단 거리보다 짧으면 갱신
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

# 그래프 표현 (인접 리스트)
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# 시작 노드 A에서 다른 모든 노드까지의 최단 거리
distances = dijkstra(graph, 'A')
print(distances)


# 다익스트라로도 풀 수 있다고


import heapq
import sys

input = sys.stdin.read
data = input().split()

# 입력 처리
n = int(data[0])
d = int(data[1])
shortcuts = []
index = 2
for _ in range(n):
    start = int(data[index])
    end = int(data[index + 1])
    length = int(data[index + 2])
    if end <= d:  # 고속도로 끝을 넘어서는 지름길은 무시
        shortcuts.append((start, end, length))
    index += 3

# 다익스트라 알고리즘을 위한 초기화
distances = [float('inf')] * (d + 1)
distances[0] = 0
priority_queue = [(0, 0)]

# 다익스트라 알고리즘 실행
while priority_queue:
    current_distance, current_node = heapq.heappop(priority_queue)

    if current_distance > distances[current_node]:
        continue

    # 기본 고속도로 경로 처리
    if current_node + 1 <= d:
        next_distance = current_distance + 1
        if next_distance < distances[current_node + 1]:
            distances[current_node + 1] = next_distance
            heapq.heappush(priority_queue, (next_distance, current_node + 1))

    # 지름길 처리
    for start, end, length in shortcuts:
        if current_node == start and end <= d:
            next_distance = current_distance + length
            if next_distance < distances[end]:
                distances[end] = next_distance
                heapq.heappush(priority_queue, (next_distance, end))

# 최종 결과 출력
print(distances[d])
