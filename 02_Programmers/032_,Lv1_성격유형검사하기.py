
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/118666

from collections import defaultdict

def solution(survey, choices):
    answer = ''
    scores = [3, 2, 1, 0, 1, 2, 3]
    table = defaultdict(int)

    def max_alpha(alpha1, alpha2):
        if table[alpha1] >= table[alpha2]:
            return alpha1
        elif table[alpha1] < table[alpha2]:
            return alpha2

    for surv, choice in zip(survey, choices):
        if choice <= 3:
            table[str(surv[0])] += scores[choice - 1]
        elif choice >= 5:
            table[str(surv[1])] += scores[choice - 1]

    answer += max_alpha("R", "T")
    answer += max_alpha("C", "F")
    answer += max_alpha("J", "M")
    answer += max_alpha("A", "N")

    return answer