
# 문제 링크: https://www.acmicpc.net/problem/1268

import sys
from collections import defaultdict

input = sys.stdin.readline
N = int(input())
class_nums = []

answers = defaultdict(int)
for _ in range(N):
    class_nums.append(list(map(int, input().split())))
mates = [set() for _ in range(N)]

for grade in range(5):
    idx_class_nums = defaultdict(list)
    for i in range(N):
        cur_class_num = class_nums[i][grade]
        idx_class_nums[cur_class_num].append(i)
    for persons in idx_class_nums.values():
        if len(persons) >= 2:
            for person in persons:
                mates[person].update(set(persons)-{person})
max_cnt = -1
answer_person = 0

for i in range(N):
    cnt = len(mates[i])
    if cnt > max_cnt or (cnt == max_cnt and i < answer_person):
        max_cnt = cnt
        answer_person = i
print(answer_person + 1)