
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/138476

from collections import Counter

def solution(k, tangerine):
    answer = 0
    result = 0
    for gul in Counter(tangerine).most_common():
        k -= gul[1]
        result += 1
        if k <= 0:
            break
    return result