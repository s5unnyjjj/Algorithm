
# 문제 링크: https://www.acmicpc.net/problem/1309

import sys
input = sys.stdin.readline

N = int(input())

dp = [0 for _ in range(N+1)]

dp[0] = 1
dp[1] = 3
for i in range(2, N+1):
    dp[i] = (2*dp[i-1] + dp[i-2])%9901
print(dp[N])