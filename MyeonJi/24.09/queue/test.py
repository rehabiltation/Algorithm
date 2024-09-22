from collections import deque
test = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test = deque(test)
for i in range(len(test)):
    test.rotate(i+1)
    print(i+1)
    print(*test)