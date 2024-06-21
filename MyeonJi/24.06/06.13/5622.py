# 소요시간: 7분
# 특이사항: 알고리즘의 어려운점_문제이해가 한번에 안된다

alpabet_list = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
word = input()

ans = 0
for alpabet in alpabet_list :  
    for i in alpabet:  
        for x in word :  
            if i == x :  
                ans += alpabet_list.index(alpabet) +3  # ans = ans + index +3
print(ans)