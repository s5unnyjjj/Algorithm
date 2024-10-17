
# 문제 링크: https://www.acmicpc.net/problem/10451

import sys

input = sys.stdin.readline

T = int(input())

def dfs(start):
    visited[start] = True
    end = connections[start]-1
    if not visited[end]:
        dfs(end)

for _ in range(T):
    N = int(input())
    connections = list(map(int, input().split()))
    visited = [False] * N
    answer = 0

    for i in range(N):
        if not visited[i]:
            dfs(i)
            answer += 1
    print(answer)