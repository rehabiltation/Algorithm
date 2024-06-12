# 소요시간 : 10분
# 런타임 이슈 ㄱ-

sentence = input().split(' ')
new_list = [s for s in sentence if s]
cnt = len(new_list)
print(cnt)
