# 소요시간: 9분
# 특이사항: 컵홀더 개수 구하는 건줄; seat 리스트로 받았다가 안돼서 걍 while 돌렸어요

N = int(input())
seats = input()

# 컵홀더 개수
cnt = 1  # 첫 번째 좌석의 왼쪽에 하나를 먼저 추가
i = 0

while i < N:
    if seats[i] == 'S':
        cnt += 1
        i += 1
    elif seats[i] == 'L':
        cnt += 1
        i += 2

# 최종 결과는 컵홀더 개수와 좌석 수 중 작은 값을 사용
print(min(cnt, N))
