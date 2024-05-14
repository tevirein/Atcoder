# dungeon1では最小時間を求めたのに対し、dungeon2はたどった部屋のルートを出力する

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * N
dp[0] = 0
dp[1] = A[0]
for i in range(2, N):
    dp[i] = min(dp[i-1]+A[i-1], dp[i-2]+B[i-2])

ans = []

place = N-1
while True:
    ans.append(place)
    if place == 0:
        break

    if dp[place-1] + A[place-1] == dp[place]:
        place -= 1
    else:
        place -= 2

ans.reverse()
print(len(ans))
for j in range(len(ans)):
    print(ans[j]+1, end=" ")