
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43165

from collections import deque

def solution(numbers, target):
    answer = 0

    que = deque()
    que.append([numbers[0], 0])
    que.append([-1 * numbers[0], 0])
    n = len(numbers)

    while que:
        num, idx = que.popleft()
        idx += 1
        if idx < n:
            que.append([num + numbers[idx], idx])
            que.append([num - numbers[idx], idx])
        else:
            if num == target:
                answer += 1

    return answer