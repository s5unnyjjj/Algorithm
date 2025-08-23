
# 문제 링크: https://www.acmicpc.net/problem/1743

import sys
limit_number = 10**7
sys.setrecursionlimit(limit_number)

input = sys.stdin.readline
N, M, K = map(int, input().split())

space = [[0]*M for _ in range(N)]

for _ in range(K):
    r, c = map(int, input().split())
    space[r-1][c-1] = 1


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

food = 0

def dfs(x, y, arr):
    global food

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if space[nx][ny] == 1:
                arr.append([nx, ny])
                if food < len(arr):
                    food = len(arr)
                space[nx][ny] = 0
                dfs(nx, ny, arr)

    return

for i in range(N):
    for j in range(M):
        if space[i][j] == 1:
            space[i][j] = 0
            arr = []
            dfs(i, j, [[i, j]])

print(food)