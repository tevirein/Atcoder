# 部分和問題を動的解決法で解いたもの

N, S = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * (S+1) for _ in range(N+1)]
dp[0][0] = True

for i in range(1, N+1):
    for j in range(S+1):
        if dp[i-1][j]:
            dp[i][j] = True
        if j >= A[i-1]:
            if dp[i-1][j-A[i-1]]:
                dp[i][j] = True
        
if dp[N][S]:
    print("Yes")
else:
    print("No")