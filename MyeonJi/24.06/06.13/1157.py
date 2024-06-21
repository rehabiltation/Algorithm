# 소요시간: 14분
# 특이사항: lower를 씌우던가 붙이던가 고민함 나중에 upper랑 lower 둘다 나오길래 처음부터 upper처리

word = input().upper()
s_word = list(set(word))
cnt = []
for k in s_word:
    cnt.append(word.count(k))
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    index = cnt.index(max(cnt))
    print(s_word[index])

'''
런타임에러 ㄱ-
word = input().upper()
alpabet_list = list(set(word))
count_list = []

for a in alpabet_list:
    count_list.append(word.count(a))

if count_list(max(count_list)) > 1:
    print("?")
else:
    print(alpabet_list[count_list.index(max(count_list))])
    '''