
# 문제 링크: https://www.acmicpc.net/problem/1085

import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))