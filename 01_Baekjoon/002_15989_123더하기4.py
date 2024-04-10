
# 문제 링크: https://www.acmicpc.net/problem/15989
# 코드 설명: https://s5unnyjjj.tistory.com/88

import sys
input = sys.stdin.readline

T = int(input())
MAX_VALUE = 10001
dp = [1]*MAX_VALUE
dp[2] = 2

for i in range(3, MAX_VALUE):
    dp[i] += (i//2 + i//3)
    if i >= 5:
        dp[i] += dp[i-5]
for _ in range(T):
    n = int(input())
    print(dp[n])