# 문제

"""
L과 R이 주어진다. 이때, L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.
"""

# 입력

# 첫째 줄에 L과 R이 주어진다. L은 2,000,000,000보다 작거나 같은 자연수이고, R은 L보다 크거나 같고, 2,000,000,000보다 작거나 같은 자연수이다.

# 출력

# 첫째 줄에 L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.

# 정답

L, R = input().split()

int_L = int(L)
int_R = int(R)

len_L = len(L)
len_R = len(R)

ans = 0

if len_L < len_R:
    ans = 0
else:
    for i in range(len_L):
        if L[i] == R[i] and L[i] == '8':
            if L[i] == R[i]:
                ans += 1
        elif L[i] < R[i]:
            break

print(ans)