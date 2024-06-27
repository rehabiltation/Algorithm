N = int(input())
tg = int(input())

# 숫자를 채울 배열 만들기
arr = [[0] * N for _ in range(N)]

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

# num: 시작값, i,j: 인덱스, dr: 방향
num = N * N
i , j = 0, 0
dr = 0
# 지정 값 인덱스
ny, nx = 0, 0

# num이 0이 되기 이전까지 while문 실행
while num > 0:
    arr[i][j] = num
    # 지정값에 해당하면 인덱스 저장
    if num == tg:
        ny, nx = i + 1, j + 1
    # 범위를 벗어나거나 0이 아니면 방향을 변경한다.
    if i + dy[dr] < 0 or i + dy[dr] >= N or j + dx[dr] < 0 or j + dx[dr] >= N or arr[i + dy[dr]][j + dx[dr]] != 0:
        dr = (dr + 1) % 4
    i += dy[dr]
    j += dx[dr]
    num -= 1

for i in arr:
    print(*i)

print(ny, nx)