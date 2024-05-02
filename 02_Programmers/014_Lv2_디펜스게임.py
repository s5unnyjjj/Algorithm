
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/142085
# 코드 설명: https://s5unnyjjj.tistory.com/106

"""
기본 배열을 사용한 경우 -> 시간초과
"""
def solution(n, k, enemy):
    answer = 0
    heap = []
    sum_enemy = 0

    for en in enemy:
        heap.append(en)
        sum_enemy += en
        if sum_enemy > n:
            if k == 0:
                break
            max_value = max(heap)
            sum_enemy -= max_value
            heap.remove(max_value)
            k -= 1
        answer += 1

    return answer


"""
heapq를 사용한 경우
"""
import heapq

def solution(n, k, enemy):
    answer = 0
    heap = []
    sum_enemy = 0

    for en in enemy:
        heapq.heappush(heap, -en)
        sum_enemy += en
        if sum_enemy > n:
            if k == 0:
                break
            sum_enemy += heapq.heappop(heap)
            k -= 1
        answer += 1

    return answer