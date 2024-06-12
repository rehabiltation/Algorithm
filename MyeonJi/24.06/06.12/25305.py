# 소요시간 : 6분
# 정렬하는 거 뭐였지?????

N, K = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort(reverse=True)
print(scores[K-1])

'''
import heapq

def findscore(N, k, scores):
    min_heap = []
    for score in scores:
        heapq.heappush(min_heap, score)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap[0]
'''