
# 문제 링크: https://www.acmicpc.net/problem/1520

import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
M, N = map(int, input().split())
maps = []

for _ in range(M):
    maps.append(list(map(int, input().split())))
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
ans = 0

dp = [[-1 for _ in range(N+1)] for _ in range(M+1)]

def dfs(x, y):
    global dp
    if x == 0 and y == 0:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if maps[nx][ny] > maps[x][y]:
                    dp[x][y] += dfs(nx, ny)
    return dp[x][y]

print(dfs(M-1, N-1))
