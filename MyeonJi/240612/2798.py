# 소요시간: 10분
# 브루트포스가 뭐게

N, M = map(int, input().split())
cards = list(map(int, input().split()))
res = 0

for i in range(N-2):
	for j in range(i+1, N-1):
		for k in range(j+1, N):
			if (cards[i] + cards[j] + cards[k] <= M):
				res = max(res, cards[i] + cards[j] + cards[k])
print(res)