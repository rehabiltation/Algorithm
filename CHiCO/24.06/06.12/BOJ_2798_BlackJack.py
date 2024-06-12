from itertools import combinations
N, M = map(int, input().split())

arr = list(input().split())

arr_list = list(combinations(arr,3))
ans = 0
for i in range(len(arr_list)):
    sum_list = (int(arr_list[i][1])+int(arr_list[i][2])+int(arr_list[i][0]))
    if sum_list <= M:
        if sum_list > ans:
            ans = sum_list
print(ans)