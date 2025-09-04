
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    before_num = arr[0]
    new_arr = [before_num]
    for v in arr:
        if v != before_num:
            before_num = v
            new_arr.append(v)
    return new_arr