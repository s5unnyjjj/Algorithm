

# 문제 링크: https://www.acmicpc.net/problem/11660

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
table = []
dp = [[0 for _ in range(N+2)] for _ in range(N+2)]

for _ in range(N):
    table.append(list(map(int, input().split())))

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1] + table[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = list(map(int, input().split()))
    print(dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] +dp[x1-1][y1-1])