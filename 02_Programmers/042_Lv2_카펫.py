
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    answer = []
    sum_xy = (brown + 4) // 2

    for i in range(1, sum_xy):
        x = i
        y = sum_xy - i
        if x < y:
            continue
        if x * y == brown + yellow:
            answer.append([x, y])

    return answer[0]