# 소요시간: 3분 40초
# 문자열 뒤집기 까묵음

A, B = input().split()
newA, newB = A[::-1], B[::-1]
if int(newA) > int(newB):
    ans = int(newA)
else:
    ans = int(newB)
print(ans)