# 소요시간: 
# 특이사항: int(input())으로 받았다가 리스트안돼서 런타임남

while True:
    num1 = input()
    num_list = list(reversed(num1))
    num2 = int(''.join(num_list))

    if num1 == "0":
        break

    if int(num1) == num2:
        print("yes")
    else:
        print("no")