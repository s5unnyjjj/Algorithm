
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/169199
# 코드 설명: https://s5unnyjjj.tistory.com/103

from collections import deque

direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def moving(pos, di, board):
    lenY, lenX = len(board), len(board[0])
    cx, cy = pos[0], pos[1]
    nx, ny = pos[0], pos[1]
    if di[0] == 0:
        for i in range(1, lenX):
            ndi = di[1] * i
            if 0 <= cy + ndi < lenX:
                if board[cx][cy + ndi] == 'D':
                    nx, ny = cx, cy + di[1] * (i - 1)
                    break
                if cy + ndi == (lenX - 1):
                    nx, ny = cx, lenX - 1
                    break
                if cy + ndi == 0:
                    nx, ny = cx, 0
                    break
            else:
                break

    elif di[1] == 0:
        for i in range(1, lenY):
            ndi = di[0] * i
            if 0 <= cx + ndi < lenY:
                if board[cx + ndi][cy] == 'D':
                    nx, ny = cx + di[0] * (i - 1), cy
                    break
                if cx + ndi == (lenY - 1):
                    nx, ny = lenY - 1, cy
                    break
                if cx + ndi == 0:
                    nx, ny = 0, cy
                    break
            else:
                break
    return nx, ny


def bfs(cur_pos, end_pos, board, visited):
    que = deque()
    que.append(cur_pos)
    visited[cur_pos[0]][cur_pos[1]] = 0
    while que:
        cx, cy = que.popleft()
        for di in direct:
            nx, ny = moving([cx, cy], di, board)
            if [nx, ny] == end_pos:
                return visited[cx][cy] + 1
            elif visited[cx][cy] + 1 < visited[nx][ny]:
                que.append([nx, ny])
                visited[nx][ny] = visited[cx][cy] + 1
    return -1


def solution(board):
    start_pos, end_pos = [], []
    lenY, lenX = len(board), len(board[0])
    visited = [[float('inf') for _ in range(lenX)] for _ in range(lenY)]

    for i in range(lenY):
        for j in range(lenX):
            if board[i][j] == 'R':
                start_pos = [i, j]
                visited[i][j] = 1
            elif board[i][j] == 'G':
                end_pos = [i, j]
            if start_pos and end_pos:
                break

    ans = bfs(start_pos, end_pos, board, visited)
    return ans