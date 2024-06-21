# 소요시간: 8분
# 특이사항: 덩치 비교를 왜 해야함???

N = int(input())
arr = []

for _ in range(N):
    x, y = map(int, input().split())
    arr.append([x, y])

ranks = [1] * N

for i in range(N):
    for j in range(N):
        if i != j: # 내가 아닐 때
            if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
                ranks[i] += 1

# 결과 출력
print(' '.join(map(str, ranks)))
