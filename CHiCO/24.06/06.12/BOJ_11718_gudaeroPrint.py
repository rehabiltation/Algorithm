# A = input()
# while True:
#     if A:
#         print(A)
#     else:
#         break

# 입력이 안정해져 있을때는 try except구문 사용하라고 합니다.
while True:
    try:
        A = input()
        print(A)
    except:
        break