
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque

def solution(priorities, location):
    answer = 0
    que = deque([(v, i) for i, v in enumerate(priorities)])

    while que:
        cur_p, cur_i = que.popleft()
        if que and cur_p < max([p for p, _ in que]):
            que.append((cur_p, cur_i))
        else:
            answer += 1
            if cur_i == location:
                return answer

    return answer