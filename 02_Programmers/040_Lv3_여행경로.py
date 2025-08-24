
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43164

answer = []

def dfs(start, tickets, path):
    global answer

    if len(tickets) == 1:
        path.extend(tickets[0])
        answer.append(path)
        return

    for ticket in tickets:
        if start == ticket[0]:
            idx = tickets.index(ticket)
            tickets.remove(ticket)
            dfs(ticket[1], tickets, path + [start])
            tickets.insert(idx, ticket)
    return


def solution(tickets):
    start_idx = [idx for idx, ticket in enumerate(tickets) if ticket[0] == "ICN"]
    for idx in start_idx:
        start, end = tickets[idx]
        tickets.remove(tickets[idx])
        dfs(end, tickets, [start])
        tickets.insert(idx, [start, end])

    answer.sort()

    return answer[0]