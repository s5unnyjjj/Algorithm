
# 문제 링크: https://www.acmicpc.net/problem/1475

import sys

input = sys.stdin.readline

N = list(input())[:-1]
from collections import Counter
counter = Counter(N)
counter_mc = counter.most_common()
nums = [v[0] for v in counter_mc if v[1] == counter_mc[0][1]]

answer = 0
if '6' in nums or '9' in nums:
    sum_counter = counter['6'] + counter['9']
    answer = (sum_counter//2) + (sum_counter%2)
    if '6' in nums: nums.remove('6')
    if '9' in nums: nums.remove('9')
    if nums:    answer = max(answer, counter[nums[0]])
    print(answer)
else:
    print(counter_mc[0][1])


"""
첫번째 시도 -> 반례 생각 하는 연습 기르고자 생각해 본 반례 예시들
 (반례1) 6006 -> 2
 (반례2) 11669966 -> 4
 (반례3) 111669999 -> 3
 (반례4) 888666999 -> 2
 (반례5) 126699999 -> 4
 
import sys

input = sys.stdin.readline

N = list(input())[:-1]
from collections import Counter
counter = Counter(N)
counter_mc = counter.most_common()

if counter_mc[0][0] == '6' or counter_mc[0][0] == '9':
    sum_counter = counter['6'] + counter['9']
    print((sum_counter//2) + (sum_counter%2))
else:
    print(counter_mc[0][1])

"""
