
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/176963

def solution(name, yearning, photo):
    answer = []
    scores = {}

    for n, y in zip(name, yearning):
        scores[n] = y

    for pho in photo:
        score = 0
        for p in pho:
            if p in scores.keys():
                score += scores[p]
        answer.append(score)
    return answer