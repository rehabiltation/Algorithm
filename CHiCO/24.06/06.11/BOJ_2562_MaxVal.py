MaxVal = 0
Maxnum = 0
for i in range(9):
    n = int(input())
    if n > MaxVal:
        MaxVal = n
        Maxnum = i+1

print(MaxVal)
print(Maxnum)