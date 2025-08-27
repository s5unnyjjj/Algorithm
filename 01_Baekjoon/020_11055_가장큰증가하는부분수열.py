
# 문제 링크: https://www.acmicpc.net/problem/11055

import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int, input().split()))
dp = [0 for _ in range(N+1)]
dp[0] = arr[0]
for i in range(1, N):
    tmp = []
    for j in range(i-1, -1, -1):
        if arr[i] > arr[j]:
            tmp.append(dp[j])
    if not tmp:
        dp[i] = arr[i]
    else:
        dp[i] = max(tmp)+arr[i]
print(max(dp))