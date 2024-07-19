# 문제

"""
지민이는 항구에서 일한다. 그리고 화물을 배에 실어야 한다. 모든 화물은 박스에 안에 넣어져 있다. 항구에는 크레인이 N대 있고, 1분에 박스를 하나씩 배에 실을 수 있다. 모든 크레인은 동시에 움직인다.

각 크레인은 무게 제한이 있다. 이 무게 제한보다 무거운 박스는 크레인으로 움직일 수 없다. 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 구하는 프로그램을 작성하시오.
"""

# 입력

"""
첫째 줄에 N이 주어진다. N은 50보다 작거나 같은 자연수이다. 둘째 줄에는 각 크레인의 무게 제한이 주어진다. 이 값은 1,000,000보다 작거나 같다. 셋째 줄에는 박스의 수 M이 주어진다. M은 10,000보다 작거나 같은 자연수이다. 넷째 줄에는 각 박스의 무게가 주어진다. 이 값도 1,000,000보다 작거나 같은 자연수이다.
"""

# 출력

# 첫째 줄에 모든 박스를 배로 옮기는데 드는 시간의 최솟값을 출력한다. 만약 모든 박스를 배로 옮길 수 없으면 -1을 출력한다.

# 정답

# 시간초과
"""
import sys
input = sys.stdin.readline

N = int(input())
cranes = list(map(int, input().split()))
M = int(input())
boxes = list(map(int, input().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0] < boxes[0]:
    ans = -1

time = 0

while boxes:
    time += 1
    crane_index = 0
    box_index = 0

    while box_index < len(boxes):
        if crane_index == N:
            break
        if cranes[crane_index] >= boxes[box_index]:
            boxes.pop(box_index)
            crane_index += 1
        else:
            box_index += 1

ans = time

print(ans)
"""

# 정답

def min_time_to_move_boxes(N, crane_limits, M, box_weights):
    # 크레인 무게 제한과 박스 무게를 내림차순으로 정렬
    crane_limits.sort(reverse=True)
    box_weights.sort(reverse=True)
    
    # 가장 무거운 박스를 가장 큰 크레인이 들 수 없다면 -1 반환
    if box_weights[0] > crane_limits[0]:
        return -1
    
    # 시간을 측정하기 위한 변수 초기화
    time = 0
    
    # 남은 박스가 있을 때까지 반복
    while box_weights:
        time += 1
        crane_index = 0
        for box in box_weights[:]:
            if crane_index == N:
                break
            if crane_limits[crane_index] >= box:
                box_weights.remove(box)
                crane_index += 1
    
    return time

# 입력 처리
N = int(input().strip())
crane_limits = list(map(int, input().strip().split()))
M = int(input().strip())
box_weights = list(map(int, input().strip().split()))

# 결과 출력
print(min_time_to_move_boxes(N, crane_limits, M, box_weights))

# 시간 초과 이유
"""
첫 번째 코드:

요소를 제거할 때마다 pop 연산이 수행되며, 리스트의 크기가 줄어들면서 매 반복마다 
O(n)의 시간이 소요됩니다.
최악의 경우 𝑂(𝑛2)의 시간 복잡도를 가질 수 있습니다.

두 번째 코드:

얕은 복사본을 사용하여 리스트를 반복하면서, 필요한 경우에만 remove 연산을 수행합니다.
리스트의 크기에 비례하여 한 번씩만 요소를 제거하므로, 전체 시간 복잡도는 
𝑂(𝑛⋅𝑚)로 더 효율적입니다.

무슨말인지 잘 모르겠다
"""