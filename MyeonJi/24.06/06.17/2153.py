# 소요시간: 7분
# 특이사항: ord, chr 진짜 오랜만 장상호강사님이랑 하던 거 

word = input()
cnt = 0

# 입력된 단어의 알파벳 값을 합산
for w in word:
    if w.islower():
        cnt += ord(w) - 96
    else:
        cnt += ord(w) - 38

# 소수 검사
if cnt == 1:
    print("It is a prime word.")
else:
    for i in range(2, cnt):
        if cnt % i == 0:
            print("It is not a prime word.")
            break # 이거 안넣어서 문제틀림
    else:
        print("It is a prime word.")
