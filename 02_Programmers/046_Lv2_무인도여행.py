
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154540

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

from collections import deque

def bfs(x, y, maps, visited):
    que = deque()
    que.append([x, y])
    answer = int(maps[x][y])

    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if not visited[nx][ny] and maps[nx][ny] != 'X':
                    answer += int(maps[nx][ny])
                    que.append([nx, ny])
                    visited[nx][ny] = True
    return answer, visited

def solution(maps):
    answer = []
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != 'X' and not visited[i][j]:
                visited[i][j] = True
                ans, visited = bfs(i, j, maps, visited)
                answer.append(ans)

    if not answer:
        return [-1]
    else:
        return sorted(answer)