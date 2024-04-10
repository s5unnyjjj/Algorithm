
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque, defaultdict

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def bfs(x, y, max_X, max_Y, land):
    cols = set()
    cols.add(y)
    que = deque()
    que.append([x, y])
    sum_lands = 1

    while que:
        cx, cy = que.popleft()
        for di in direct:
            nx = cx + di[0]
            ny = cy + di[1]
            if 0 <= nx < max_X and 0 <= ny < max_Y:
                if land[nx][ny] == 1:
                    land[nx][ny] = 0
                    que.append([nx, ny])
                    cols.add(ny)
                    sum_lands += 1
    return land, cols, sum_lands


def solution(land):
    answer = 0
    n, m = len(land), len(land[0])
    col_land = defaultdict(int)

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                land[i][j] = 0
                land, cur_cols, cur_sum_lands = bfs(i, j, n, m, land)
                for col in cur_cols:
                    col_land[col] += cur_sum_lands
    answer = max(col_land.values())

    return answer