
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    new_s = []
    for bracket in s:
        if bracket == '(':
            new_s.append('(')
        else:
            if not new_s:
                return False
            else:
                new_s.pop()
    if new_s:
        return False
    return True

