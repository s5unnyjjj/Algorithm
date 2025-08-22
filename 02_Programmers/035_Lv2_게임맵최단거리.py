
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(maps):
    que = deque()
    que.append([0, 0])

    while que:
        cx, cy = que.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] == 1:
                    que.append([nx, ny])
                    maps[nx][ny] = maps[cx][cy] + 1
                # elif maps[nx][ny] > 1:
                #     if maps[nx][ny] > maps[cx][cy] + 1:
                #         que.append([nx, ny])
                #         maps[nx][ny] = maps[cx][cy] + 1
    return maps[-1][-1]

def solution(maps):
    answer = bfs(maps)

    if answer == 1:
        return -1
    else:
        return answer