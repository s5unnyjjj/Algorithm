
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/154538
# 코드 설명: https://s5unnyjjj.tistory.com/109

"""
Try #1 - RESULT: FAIL(RuntimeError)
"""
def solution(x, y, n):
    answer = -1

    def dfs(src, cnt):
        nonlocal answer
        if src == y:
            if answer == -1:
                answer = cnt
            else:
                answer = min(answer, cnt)
            return
        else:
            if src+n <= y:
                dfs(src+n, cnt+1)
            if src * 2 <= y:
                dfs(src*2, cnt+1)
            if src * 3 <= y:
                dfs(src*3, cnt+1)
        return

    dfs(x, 0)

    return answer

"""
Try #2 - RESULT: SUCCESS
"""
def solution(x, y, n):
    dp = [-1 for _ in range(max(y + n, y * 2, y * 3) + 1)]
    dp[x] = 0

    for i in range(x, y):
        if dp[i] == -1:
            continue

        if dp[i * 2] != -1:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        else:
            dp[i * 2] = dp[i] + 1

        if dp[i * 3] != -1:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
        else:
            dp[i * 3] = dp[i] + 1

        if dp[i + n] != -1:
            dp[i + n] = min(dp[i + n], dp[i] + 1)
        else:
            dp[i + n] = dp[i] + 1

    return dp[y]