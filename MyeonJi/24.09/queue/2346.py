## 문제를 이해못해서 한참 걸림 ... ㅠㅠ
from collections import deque

# 입력 받기
N = int(input())
arr = list(map(int, input().split()))

# 풍선 번호를 1부터 N까지 deque로 저장
q = deque((i+1, arr[i]) for i in range(N))

result = []

# 첫 번째 풍선 터뜨리기
while q:
    # 현재 풍선 터뜨리기
    idx, num = q.popleft()
    result.append(idx)
    
    # 풍선이 더 없다면 종료
    if not q:
        break

    # 이동할 수를 양수, 음수에 따라 rotate로 처리
    if num > 0:
        q.rotate(-(num - 1))  # 양수인 경우 오른쪽으로 num - 1만큼 이동
    else:
        q.rotate(-num)  # 음수인 경우 그대로 이동

# 결과 출력
print(*result)
