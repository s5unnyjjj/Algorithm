
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131130

def solution(cards):
    cand = []
    visited = [False] * (len(cards)+1)

    for card in cards:
        if not visited[card]:
            group = []
            visited[card] = True
            while True:
                if card in group:
                    break
                else:
                    group.append(card)
                    card = cards[card -1]
                visited[card] = True
            group_size = len(group)
            cand.append(group_size)

    if cand[0] == len(cards):
        return 0

    cand.sort(reverse=True)
    return cand[0] * cand[1]