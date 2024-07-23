# 문제

"""
수직선 위에 N개의 좌표 X1, X2, ..., XN이 있다. 이 좌표에 좌표 압축을 적용하려고 한다.

Xi를 좌표 압축한 결과 X'i의 값은 Xi > Xj를 만족하는 서로 다른 좌표 Xj의 개수와 같아야 한다.

X1, X2, ..., XN에 좌표 압축을 적용한 결과 X'1, X'2, ..., X'N를 출력해보자.
"""

# 입력

"""
첫째 줄에 N이 주어진다.

둘째 줄에는 공백 한 칸으로 구분된 X1, X2, ..., XN이 주어진다.
"""

# 출력

# 첫째 줄에 X'1, X'2, ..., X'N을 공백 한 칸으로 구분해서 출력한다.

# 시간초과남

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int,input().split()))

n_arr = sorted(set(arr))
m_dict = {}

for i in n_arr:
    m_dict[i] = n_arr.index(i)

ans_list = []
for i in arr:
    ans_list.append(m_dict[i])

print(*ans_list)

# 정답

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 중복 제거 후 정렬
n_arr = sorted(set(arr))

# 딕셔너리를 한번에 생성
# enumerate로 생성해야 시간초과가 안난다고 함.
m_dict = {value: index for index, value in enumerate(n_arr)}

# 결과 리스트 생성
ans_list = [m_dict[i] for i in arr]

# 결과 출력
print(*ans_list)
