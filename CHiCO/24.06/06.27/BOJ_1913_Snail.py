# 문제

"""
홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.

9	2	3
8	1	4
7	6	5
25	10	11	12	13
24	9	2	3	14
23	8	1	4	15
22	7	6	5	16
21	20	19	18	17
N이 주어졌을 때, 이러한 표를 출력하는 프로그램을 작성하시오. 또한 N2 이하의 자연수가 하나 주어졌을 때, 그 좌표도 함께 출력하시오. 예를 들어 N=5인 경우 6의 좌표는 (4,3)이다.
"""

# 입력 

# 첫째 줄에 홀수인 자연수 N(3 ≤ N ≤ 999)이 주어진다. 둘째 줄에는 위치를 찾고자 하는 N2 이하의 자연수가 하나 주어진다.

# 출력

# N개의 줄에 걸쳐 표를 출력한다. 각 줄에 N개의 자연수를 한 칸씩 띄어서 출력하면 되며, 자릿수를 맞출 필요가 없다. N+1번째 줄에는 입력받은 자연수의 좌표를 나타내는 두 정수를 한 칸 띄어서 출력한다.

# 정답

N = int(input())
find = int(input())


arr = [[0] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


x, y = 0, 0  
direction = 0  
num = N * N  

while num > 0:
    arr[x][y] = num
    if num == find:
        target_x, target_y = x + 1, y + 1
    num -= 1
    
    nx, ny = x + dx[direction], y + dy[direction]
    
    if nx < 0 or ny < 0 or nx >= N or ny >= N or arr[nx][ny] != 0:
        # 이렇게 해서 어느쪽으로 갈지를 바꿔줄 수 있대요. 이걸 해결 못했었네요.
        # 처음에는 지금 방향을 문자로 놓고 바꿔주려고 했었는데 이렇게 하면 되네요.
        direction = (direction + 1) % 4
        nx, ny = x + dx[direction], y + dy[direction]
    
    x, y = nx, ny

for row in arr:
    print(" ".join(map(str, row)))

print(target_x, target_y)
