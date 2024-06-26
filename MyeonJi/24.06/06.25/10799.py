# 소요시간:
# 특이사항: 왜 익숙하지? swea에서 봤나

N = input()
stack=[]
cnt = 0

for i in range(len(N)):
    if N[i] == "(":
        stack.append("(")
    else :
        if N[i-1] == "(":
            stack.pop()
            cnt += len(stack)
            
        else :
            stack.pop()
            cnt += 1 
print(cnt)