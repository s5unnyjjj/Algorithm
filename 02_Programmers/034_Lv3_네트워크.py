
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def bfs(start_node, computers, visited):
    que = deque()
    que.append(start_node)
    visited[start_node] = True

    while que:
        cur_node = que.popleft()
        for i, computer in enumerate(computers[cur_node]):
            if computer == 1 and not visited[i] and i != start_node:
                que.append(i)
                visited[i] = True

def solution(n, computers):
    answer = 0

    visited = [False] * n

    for i, computer in enumerate(computers):
        if not visited[i]:
            bfs(i, computers, visited)
            answer += 1

    return answer