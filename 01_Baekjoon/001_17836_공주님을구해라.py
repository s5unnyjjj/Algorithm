
# 문제 링크: https://www.acmicpc.net/problem/17836
# 코드 설명: https://s5unnyjjj.tistory.com/83

import sys
from collections import deque
input = sys.stdin.readline

N, M, T = list(map(int, input().split()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
graph = []
pos_gram = []
for i in range(N):
    tmp = list(map(int, input().split()))
    if 2 in tmp:
        pos_gram = [i, tmp.index(2)]
    graph.append(tmp)

MAX_VALUE = 100001
def bfs():
    que = deque()
    que.append([0, 0])
    visited = [[MAX_VALUE]*M for _ in range(N)]
    visited[0][0] = 0

    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if graph[nx][ny] != 1 and visited[nx][ny] == MAX_VALUE:
                    visited[nx][ny] = visited[cx][cy] + 1
                    que.append([nx, ny])
    return visited

return_visited = bfs()
no_gram = return_visited[N-1][M-1]
yes_gram = return_visited[pos_gram[0]][pos_gram[1]] + abs((N-1)-pos_gram[0]) + abs((M-1)-pos_gram[1])
answer = min(no_gram, yes_gram)

if answer > T:
    print('Fail')
else:
    print(answer)