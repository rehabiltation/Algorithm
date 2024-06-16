# 소요시간: 
# 특이사항: 9달 전에 풀었던 문제라네영

N = int(input())
for tc in range(1, N+1):
    sentence = list(input().split(' '))

    stack = []
    new_lst = []

    for s in sentence:
        stack.append(s)

    for s in range(len(sentence)):
        a = stack.pop()
        new_lst.append(a)

    print(f'Case #{tc}:', *new_lst)