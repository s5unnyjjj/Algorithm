
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons

def solution(n, w, num):
    answer = 0
    size_y = n // w + 1
    direction = 'L'
    value_idx = [-1, -1]

    for value in range(n):
        row = (size_y - (value // w)) -1
        col = 0
        if direction == 'L':
            col = value%w
        elif direction == 'R':
            col = w-(value%w)-1
        if (value+1) % w == 0:
            if direction == 'R':    direction = 'L'
            else:   direction = 'R'
        if (value+1) == num:
            value_idx = [row, col]
        if value_idx[1] == col:
            answer += 1

    return answer

