
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/250121

def solution(data, ext, val_ext, sort_by):
    answer = []
    data_idx = {"code":0, "date":1, "maximum":2, "remain":3}
    for values in data:
        if values[data_idx[ext]] < val_ext:
            answer.append(values)

    answer.sort(key=lambda x:x[data_idx[sort_by]])
    return answer
