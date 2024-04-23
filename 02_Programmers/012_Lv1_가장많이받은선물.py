
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/258712

from collections import defaultdict, Counter

def solution(friends, gifts):
    answer = defaultdict(int)
    gift_score = defaultdict(int)
    table = defaultdict(list)

    for gift in gifts:
        p1, p2 = gift.split(" ")
        table[p1].append(p2)
        gift_score[p1 + "give"] += 1
        gift_score[p2 + "recv"] += 1

    for i, f1 in enumerate(friends):
        for f2 in friends[i + 1:]:
            if f1 != f2:
                n1, n2 = Counter(table[f1])[f2], Counter(table[f2])[f1]
                if n1 < n2:
                    answer[f2] += 1
                elif n1 > n2:
                    answer[f1] += 1
                else:
                    s1 = gift_score[f1 + "give"] - gift_score[f1 + "recv"]
                    s2 = gift_score[f2 + "give"] - gift_score[f2 + "recv"]
                    if s1 > s2:
                        answer[f1] += 1
                    elif s1 < s2:
                        answer[f2] += 1

    if answer:
        return max(answer.values())
    return 0