
# 문제 링크: https://www.acmicpc.net/problem/1261

import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

rooms = []
for _ in range(N):
    row = list(map(int, list(input().strip())))
    rooms.append(row)

change = [[-1]*N for _ in range(N)]
change[0][0] = 0

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    que = deque()
    que.append([0, 0])

    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if change[nx][ny] == -1:
                    if rooms[nx][ny] == 1:
                        change[nx][ny] = change[cx][cy]
                        que.appendleft([nx, ny])
                    else:
                        change[nx][ny] = change[cx][cy] + 1
                        que.append([nx, ny])


bfs()

print(change[N-1][N-1])