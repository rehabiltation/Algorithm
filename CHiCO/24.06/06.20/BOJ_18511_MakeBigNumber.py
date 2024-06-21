# 문제

"""
N보다 작거나 같은 자연수 중에서, 집합 K의 원소로만 구성된 가장 큰 수를 출력하는 프로그램을 작성하시오. K의 모든 원소는 1부터 9까지의 자연수로만 구성된다.

예를 들어 N=657이고, K={1, 5, 7}일 때 답은 577이다.
"""

# 입력

"""
첫째 줄에 N, K의 원소의 개수가 공백을 기준으로 구분되어 자연수로 주어진다. (10 ≤ N ≤ 100,000,000, 1 ≤ K의 원소의 개수 ≤ 3) 둘째 줄에 K의 원소들이 공백을 기준으로 구분되어 주어진다. 각 원소는 1부터 9까지의 자연수다.

단, 항상 K의 원소로만 구성된 N보다 작거나 같은 자연수를 만들 수 있는 경우만 입력으로 주어진다.
"""


# 출력

# 첫째 줄에 N보다 작거나 같은 자연수 중에서, K의 원소로만 구성된 가장 큰 수를 출력한다.

# 정답

N ,K = input().split()
K_list = list(map(int, input().split()))
K_list.sort(reverse=True)
ans_list = []
for num in N:
    num = int(num)
    print(num)
    flag = 0
    for i in K_list:
        if i <= num: # 클 때 안해줌 클때도 해줘야함
            if i == num:
                flag = 1
            if not flag:
                ans_list.append(str(i))
            else:
                if i <= num:
                    ans_list.append(str(K_list[0]))
                    print('ji')
                else:
                    ans_list.pop()
                    ans_list = str(K_list[0])*(len(N)-1)
                    print*('cje')
            break
print(''.join(ans_list))

