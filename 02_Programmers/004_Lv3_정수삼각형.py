
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 코드 설명: https://s5unnyjjj.tistory.com/86

def solution(triangle):
    if len(triangle) == 1:
        return triangle[0]
    answer = 0
    dp = [[0]*i for i in range(1, len(triangle)+1)]
    dp[0] = triangle[0]

    for i in range(1, len(triangle)):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        for j in range(1, i):
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    answer = max(dp[-1])

    return answer