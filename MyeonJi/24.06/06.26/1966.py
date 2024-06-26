# 소요시간:
# 특이사항: 10달 전에 풀었던..!! 

from collections import deque

t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0
    while queue:
        best = max(queue)
        front = queue.popleft()
        m -= 1

        if best == front: 
            count += 1
            if m < 0: 
                print(count)
                break

        else:   # 뽑은 숫자가 제일 큰 숫자가 아니면
            queue.append(front) # 제일 뒤로 밀려나게 됨
            if m < 0 :  # 제일 앞에서 뽑히면
                m = len(queue) - 1 # 제일 뒤로 이동
