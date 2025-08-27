
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946


answer = 0


def dfs(ck, dungeons, visited, cnt):
    global answer
    answer = max(answer, cnt)

    for i in range(len(dungeons)):
        if dungeons[i] not in visited:
            if ck >= dungeons[i][0]:
                visited.append(dungeons[i])
                dfs(ck - dungeons[i][1], dungeons, visited, cnt + 1)
                visited.remove(dungeons[i])


def solution(k, dungeons):
    dfs(k, dungeons, [], 0)

    return answer
