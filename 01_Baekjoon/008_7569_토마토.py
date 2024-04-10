
# 문제 링크: https://www.acmicpc.net/problem/17569
# 코드 설명: https://s5unnyjjj.tistory.com/99

import sys
from collections import deque, Counter
input = sys.stdin.readline

m, n, h = list(map(int, input().split()))
box = [[] for _ in range(h)]
direct = [[0, -1, 0], [0, 1, 0], [0, 0, -1], [0, 0, 1], [1, 0, 0], [-1, 0, 0]]

que = deque()
for z in range(h):
    for x in range(n):
        tmp = list(map(int, input().split()))
        box[z].append(tmp)
        for y in range(m):
            if box[z][x][y] == 1:
                que.append([z, x, y])
def bfs():
    day = 0
    while que:
        cz, cx, cy = que.popleft()
        for di in direct:
            nz = cz + di[0]
            nx = cx + di[1]
            ny = cy + di[2]
            if 0 <= nz < h and 0 <= nx < n and 0 <= ny < m:
                if box[nz][nx][ny] == 0:
                    que.append([nz, nx, ny])
                    box[nz][nx][ny] = box[cz][cx][cy] + 1
                    if day < box[nz][nx][ny]:
                        day = box[nz][nx][ny] - 1
    return day

res = bfs()

cur_zero_num = 0
for z in range(h):
    for x in range(n):
        cur_zero_num += Counter(box[z][x])[0]
if cur_zero_num > 0:
    print(-1)
else:
    print(res)