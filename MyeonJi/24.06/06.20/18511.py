# 소요시간: 아 진짜 모르겟음
# 특이사항: 중복순열은 여러 개의 원소를 가지고 순열을 만들 때, 같은 원소를 여러 번 사용할 수 있는 경우

N, K = map(int, input().split())
nums = sorted(map(int, input().split()), reverse=True)
N_str = str(N)
max_len = len(N_str)
result = [0]

def dfs(current):
    # 현재까지 구성된 숫자의 문자열: current
    if len(current) > 0 and int(current) <= N:
        # N보다 작으면 업데이트
        result[0] = max(result[0], int(current))
    if len(current) == max_len:
        return
    for digit in nums:
        # 문자열로 바꿔서 호출
        dfs(current + str(digit))

dfs("")
# 출력
print(result[0])



'''
from itertools import product # 순열 만들어주는

N,K = map(int,input().split())
arr = list(map(str,input().split()))
length = len(str(N))

while(True):
    temp = list(product( arr, repeat=length))
    answer = []

    for i in temp :
        if int("".join(i)) <= N :
            answer.append(int("".join(i)))

    if len(answer)>= 1:
        print(max(answer))
        break
    else : 
        length -=1
'''