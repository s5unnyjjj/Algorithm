
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 코드 설명: https://s5unnyjjj.tistory.com/82

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(maps):
    que = deque()
    que.append([0, 0])
    n, m = len(maps), len(maps[0])
    visited = [[0] * m for _ in range(n)]
    visited[0][0] = 1

    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if maps[nx][ny] >= 1 and visited[nx][ny] == 0:
                    if maps[nx][ny] == 1:  # 경우1. 이동하려는 곳에 방문한 적이 없는 경우
                        maps[nx][ny] = maps[cx][cy] + 1
                    else:  # 경우2. 이동하려는 곳에 방문한 적이 있어서 이미 다른 값이 있는 경우
                        maps[nx][ny] = min(maps[nx][ny], maps[cx][cy] + 1)
                    que.append([nx, ny])
                    visited[nx][ny] = 1


def solution(maps):
    answer = 0
    n, m = len(maps), len(maps[0])
    bfs(maps)
    answer = maps[n - 1][m - 1]
    if answer == 1:
        answer = -1
    return answer