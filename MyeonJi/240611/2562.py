# 소요시간: 3분 30초
# 헉... 나 sys.stdin.readline 쓰는 법 모름

numbers = []
for _ in range(9):
    i = int(input())
    numbers.append(i)
    
print(max(numbers))
print(numbers.index(max(numbers))+1)