
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131704#
# 코드 설명: # 코드 설명: https://s5unnyjjj.tistory.com/98

"""
첫번째 시도 -> 실패(일부 시간 초과)
"""
from collections import deque

def solution(order):
    answer = 0

    order = deque(order)
    assist_container = deque()
    len_order = len(order)

    idx = 1

    while idx <= len_order:
        target = order[0]
        if idx == target:
            idx += 1
            order.popleft()
            answer += 1
        elif assist_container and assist_container[-1] == target:
            assist_container.pop()
            order.popleft()
            answer += 1
        else:
            assist_container.append(idx)
            idx += 1
    while assist_container and order:
        assist_value = assist_container.pop()
        if assist_value == order[0]:
            answer += 1
            order.popleft()
        else:
            break

    return answer



"""
두번째 시도 -> 성공
"""
from collections import deque

def solution(order):
    answer = 0

    order = deque(order)
    assist_container = deque()
    len_order = len(order)

    idx = 1

    while idx <= len_order:
        target = order[0]
        if idx == target:
            idx += 1
            order.popleft()
            answer += 1
        elif assist_container and assist_container[-1] == target:
            assist_container.pop()
            order.popleft()
            answer += 1
        else:
            assist_container.append(idx)
            idx += 1
    while assist_container and order:
        assist_value = assist_container.pop()
        if assist_value == order[0]:
            answer += 1
            order.popleft()
        else:
            break

    return answer
