# 문제 

"""
세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.

예를 들어 A = 150, B = 266, C = 427 이라면 A × B × C = 150 × 266 × 427 = 17037300 이 되고, 계산한 결과 17037300 에는 0이 3번, 1이 1번, 3이 2번, 7이 2번 쓰였다.
"""

# 입력

# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.

# 출력

# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

# 정답

A = int(input())
B = int(input())
C = int(input())

ans = str(A*B*C)
cnt0 = 0
cnt1 = 0
cnt2 = 0
cnt3 = 0
cnt4 = 0
cnt5 = 0
cnt6 = 0
cnt7 = 0
cnt8 = 0
cnt9 = 0

for i in ans:
    if i == '0':
        cnt0 += 1
    elif i == '1':
        cnt1 += 1
    elif i == '2':
        cnt2 += 1
    elif i == '3':
        cnt3 += 1
    elif i == '4':
        cnt4 += 1
    elif i == '5':
        cnt5 += 1
    elif i == '6':
        cnt6 += 1
    elif i == '7':
        cnt7 += 1
    elif i == '8':
        cnt8 += 1
    elif i == '9':
        cnt9 += 1

print(cnt0)
print(cnt1)
print(cnt2)
print(cnt3)
print(cnt4)
print(cnt5)
print(cnt6)
print(cnt7)
print(cnt8)
print(cnt9)
