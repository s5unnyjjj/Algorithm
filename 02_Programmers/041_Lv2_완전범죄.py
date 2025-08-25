
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/389480
answer = [121, 121]

def solution(info, n, m):
    stolen = set()

    def dfs(i, a, b):
        global answer
        if b >= m or a >= n:
            return
        if (i, a, b) in stolen:
            return

        stolen.add((i, a, b))

        if i == len(info):
            if answer[0] > a:
                answer = [a, b]
            return

        dfs( i +1, a, b+ info[i][1])
        dfs(i + 1, a + info[i][0], b)
        return

    dfs(0, 0, 0)

    if answer == [121, 121]:
        return -1
    else:
        return answer[0]