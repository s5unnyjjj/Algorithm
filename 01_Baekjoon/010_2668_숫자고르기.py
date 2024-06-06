
# 문제 링크: https://www.acmicpc.net/problem/2668

import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())
table = defaultdict(int)
already_match = []
answer = []

for i in range(1, N + 1):
    table[i] = int(input())
    if i == table[i]:
        already_match.append(i)


def dfs(idx, ans_keys, ans_values):
    if idx in already_match or table[idx] in already_match:
        ans_keys.append(idx)
        return
    if idx in ans_keys:
        return
    ans_keys.append(idx)
    ans_values.add(table[idx])
    dfs(table[idx], ans_keys, ans_values)
    return


for i in range(1, N + 1):
    tmp_keys = []
    tmp_values = set()
    dfs(i, tmp_keys, tmp_values)
    if len(tmp_keys) == len(tmp_values):
        tmp_unions = set(tmp_keys).intersection(set(answer))
        if len(tmp_unions) > 0:
            continue
        answer.extend(tmp_keys)

answer.extend(already_match)
answer.sort()
print(len(answer))
for v in answer:
    print(v)