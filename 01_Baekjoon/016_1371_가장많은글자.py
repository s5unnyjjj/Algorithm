
# 문제 링크: https://www.acmicpc.net/problem/1371

import sys
from collections import defaultdict

contents = defaultdict(int)
content = sys.stdin.read()

for c in content:
    if 97 <= ord(c) <= 122:
        contents[c] += 1

contents = sorted(contents.items(), key=lambda x: [x[1], x[0]], reverse=True)

MAX_NUM = 2501
num = MAX_NUM
answer = []

for key, value in contents:
    if num != MAX_NUM and num != value:
        break
    elif num == MAX_NUM:
        answer.append(key)
        num = value
    elif num == value:
        answer.append(key)

answer = sorted(answer)
print(''.join(answer))
