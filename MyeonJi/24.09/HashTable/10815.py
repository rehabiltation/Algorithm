import sys
input = sys.stdin.readline

N = int(input())
card_dict = {}
card_list = list(map(int, input().split()))
for card in card_list:
    card_dict[card] = True

M = int(input())
arr = list(map(int, input().split()))

for a in arr:
    if a in card_dict:
        print("1")
    else:
        print("0")

