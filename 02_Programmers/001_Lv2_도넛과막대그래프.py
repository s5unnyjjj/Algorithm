
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/258711
# 코드 설명: https://s5unnyjjj.tistory.com/81

from collections import defaultdict


def solution(edges):
    answers = [0, 0, 0, 0]
    maxV = 0
    edges_in, edges_out = defaultdict(int), defaultdict(int)
    for i, j in edges:
        edges_in[i] += 1
        edges_out[j] += 1
        maxV = max(i, j, maxV)

    for i in range(1, maxV + 1):
        if edges_in[i] >= 2 and edges_out[i] >= 2:
            answers[3] += 1
        if edges_out[i] > 0 and edges_in[i] == 0:
            answers[2] += 1
        if edges_out[i] == 0 and edges_in[i] >= 2:
            answers[0] = i

    answers[1] = edges_in[answers[0]] - (answers[2] + answers[3])

    return answers