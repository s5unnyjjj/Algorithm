
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/147354

def solution(data, col, row_begin, row_end):
    answer = 0

    data = sorted(data, key=lambda x:[x[col-1], -x[0]])

    for row in range(row_begin, row_end +1):
        cur_sum = 0
        for value in data[row-1]:
            cur_sum += (value % row)
        answer = answer ^ cur_sum
    return answer