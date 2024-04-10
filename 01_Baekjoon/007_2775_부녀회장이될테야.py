
# 문제 링크: https://www.acmicpc.net/problem/2775
# 코드 설명: https://s5unnyjjj.tistory.com/98

import sys
input = sys.stdin.readline

T = int(input())
MAX_VALUE = 15
dp = [[i for i in range(1, MAX_VALUE+1)] for _ in range(1, MAX_VALUE+1)]

for a in range(1, MAX_VALUE):
    for b in range(1, MAX_VALUE):
        dp[a][b] = dp[a][b-1] + dp[a-1][b]

for _ in range(T):
    k, n = int(input()), int(input())
    print(dp[k][n-1])