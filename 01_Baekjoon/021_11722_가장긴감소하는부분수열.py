
# 문제 링크: https://www.acmicpc.net/problem/11722

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(1, N):
    tmp = []
    for j in range(i-1, -1, -1):
        if arr[i] < arr[j]:
            tmp.append(dp[j])
    if not tmp:
        dp[i] = 1
    else:
        dp[i] = max(tmp)+1
print(max(dp))