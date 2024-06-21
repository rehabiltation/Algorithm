# 소요시간:
# 특이사항: 난 수학이 너무 싫어

# 입력 처리
N = int(input())
arr = list(map(int, input().split()))
X = int(input())

# 배열 정렬
arr.sort()

# 투포인터 초기화
answer = 0
left, right = 0, N - 1

while left < right:
    temp = arr[left] + arr[right]
    
    if temp == X:
        answer += 1
        left += 1
        right -= 1
    elif temp < X:
        left += 1
    else:
        right -= 1

# 결과 출력
print(answer)

'''
# 해시맵을 이용한 쌍의 개수 찾기
seen = set()
count = 0

for num in arr:
    if (X - num) in seen:
        count += 1
    seen.add(num)

# 결과 출력
print(count)
'''