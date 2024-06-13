# 소요시간: 8분
# 특이사항: input쳤다가 시간초과떴어요

import sys

N  = int(sys.stdin.readline())
arr = [0]*10001

for _ in range(N):
    num = int(sys.stdin.readline())
    arr[num] += 1 

for i in range(10001): 
    if arr[i] != 0:
        for j in range(arr[i]): 
            print(i)

'''
시간초과 ㄱ-
N  = int(input())
arr = [0]*10001

for _ in range(N):
    num = int(input())
    arr[num] += 1 

for i in range(10001): 
    if arr[i] != 0:
        for j in range(arr[i]): 
            print(i)
'''