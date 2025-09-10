
# 문제 링크: https://www.acmicpc.net/problem/10845
import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
que = deque()
for _ in range(N):
    lines = list(input().split())
    if lines[0] == 'push':
        que.append(int(lines[1]))
    elif lines[0] == 'pop':
        if que: print(que.popleft())
        else:   print(-1)
    elif lines[0] == 'size':
        print(len(que))
    elif lines[0] == 'empty':
        if que: print(0)
        else:   print(1)
    elif lines[0] == 'front':
        if que: print(list(que)[0])
        else:   print(-1)
    elif lines[0] == 'back':
        if que: print(list(que)[-1])
        else:   print(-1)
