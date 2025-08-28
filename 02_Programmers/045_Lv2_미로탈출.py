
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/159993

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def find_pos(string_maps, length):
    leber_idx = string_maps.index("L")
    start_idx = string_maps.index("S")
    end_idx = string_maps.index("E")

    leber_pos = [leber_idx//length, leber_idx %length]
    start_pos = [start_idx//length, start_idx %length]
    end_pos = [end_idx//length, end_idx %length]
    return leber_pos, start_pos, end_pos

def bfs(start, end, maps):
    visited = [[0 ] *(len(maps[0])) for _ in range(len(maps))]
    visited[start[0]][start[1]] = 1

    que = deque()
    que.append(start)

    while que:
        cx, cy = que.popleft()
        if [cx, cy] == end:
            return visited[cx][cy]

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]):
                if maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[cx][cy] + 1
                    que.append([nx, ny])

    return visited[end[0]][end[1]]

def solution(maps):
    leber, start, end = find_pos(list("".join(maps)), len(maps[0]))
    path_start2leber = bfs(start, leber, maps)
    if path_start2leber == 0:
        return -1

    path_leber2end = bfs(leber, end, maps)
    if path_leber2end == 0:
        return -1

    return (path_start2leber + path_leber2end - 2)