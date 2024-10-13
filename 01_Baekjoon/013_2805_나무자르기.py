
# 문제 링크: https://www.acmicpc.net/problem/2805

import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
trees = list(map(int, input().split()))

left, right = 0, 1000000000
answer = -1

while left <= right:
    mid = (left + right) // 2

    return_trees = [tree-mid for tree in trees if mid < tree]

    sum_trees = sum(return_trees)
    if sum_trees >= M:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1

print(answer)