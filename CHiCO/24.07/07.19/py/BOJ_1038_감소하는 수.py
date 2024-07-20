#문제

"""
음이 아닌 정수 X의 자릿수가 가장 큰 자릿수부터 작은 자릿수까지 감소한다면, 그 수를 감소하는 수라고 한다. 예를 들어, 321과 950은 감소하는 수지만, 322와 958은 아니다. N번째 감소하는 수를 출력하는 프로그램을 작성하시오. 0은 0번째 감소하는 수이고, 1은 1번째 감소하는 수이다. 만약 N번째 감소하는 수가 없다면 -1을 출력한다.
"""

# 입력

# 첫째 줄에 N이 주어진다. N은 1,000,000보다 작거나 같은 자연수 또는 0이다.

# 출력

# 첫째 줄에 N번째 감소하는 수를 출력한다.

# 백트래킹이군

# from collections import deque

# N = int(input())
# ans_list = [0,1,2,3,4,5,6,7,8,9]
# for i in range(10,1000000):
#     arr = deque(str(i))
#     before_int = 9
#     flag = 1
#     while arr:
#         for now in arr:
#             if int(now) > before_int:
#                 flag = 0
#                 arr = []
#                 break
#             else:
#                 arr.popleft()
#             before_int = int(now)
#     if flag == 1:
#         ans_list.append(i)

# print(ans_list[N])
                

# 정답

def find_decreasing_numbers():
    decreasing_numbers = []
    
    # 백트래킹 함수 정의
    def backtrack(current_num):
        # 현재 숫자가 빈 문자열이 아니라면 감소하는 수 리스트에 추가
        if current_num != '':
            decreasing_numbers.append(int(current_num))
        
        # 현재 숫자의 마지막 자릿수가 0이라면 더 이상 감소하는 수를 만들 수 없으므로 종료
        if len(current_num) > 0 and current_num[-1] == '0':
            return
        
        # 다음 자릿수로 추가할 수 있는 숫자의 범위를 결정
        start_digit = 9 if current_num == '' else int(current_num[-1]) - 1
        
        # 가능한 숫자를 현재 숫자에 추가하며 재귀 호출
        for next_digit in range(start_digit, -1, -1):
            backtrack(current_num + str(next_digit))
    
    # 초기 호출
    backtrack('')
    
    # 생성된 감소하는 수들을 오름차순으로 정렬
    decreasing_numbers.sort()
    return decreasing_numbers

# 입력
N = int(input())

# 감소하는 수 생성
decreasing_numbers = find_decreasing_numbers()

# 결과 출력
if N < len(decreasing_numbers):
    print(decreasing_numbers[N])
else:
    print(-1)


# 백트래킹의 기본 구조

"""
def 백트래킹(n):
	if 정답이면 :
		출력 or 저장
	else :
		for 모든 자식 노드에 대해 :
			if 유망한지확인(m) :
				자식노드로 이동
				백트래킹(n+1)
				부모노드로 이동

def 유망한지확인(m):
	if 조건에 안맞으면 :
		return False
	return True
"""