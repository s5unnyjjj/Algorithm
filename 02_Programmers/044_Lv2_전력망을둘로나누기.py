
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86971

from collections import deque

def solution(n, wires):
    wires_graph = [[0] * (n + 1) for _ in range(n + 1)]

    for start, end in wires:
        wires_graph[start][end] = 1
        wires_graph[end][start] = 1

    answers = []
    for cut_wire in wires:
        que = deque()
        cut_start, cut_end = cut_wire

        visited = [cut_start]
        que.append(cut_start)

        wires_graph[cut_start][cut_end] = 0
        wires_graph[cut_end][cut_start] = 0

        while que:
            start = que.popleft()

            for i in range(n + 1):
                if i not in visited and wires_graph[start][i] == 1:
                    visited.append(i)
                    que.append(i)

        wires_graph[cut_start][cut_end] = 1
        wires_graph[cut_end][cut_start] = 1
        cur_cnt = len(visited)

        answers.append(abs(n - cur_cnt - cur_cnt))

    return min(answers)
