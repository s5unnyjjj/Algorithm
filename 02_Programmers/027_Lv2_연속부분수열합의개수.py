
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/131701
# 코드 설명: https://s5unnyjjj.tistory.com/114

"""
첫번째 시도 -> 통과(시간이 많이 소요됨)
"""
def solution(elements):
    all_set = set()

    for length in range(1, len(elements)+1):
        for start in range(len(elements)):
            summation = 0
            if start+length > len(elements):
                summation += sum(elements[start:len(elements)])
                summation += sum(elements[:start+length-len(elements)])
            else:
                summation = sum(elements[start:start+length])
            all_set.add(summation)

    answer = len(all_set)
    return answer

"""
두번째 시도 -> 통과(소요 시간 감소)
"""
def solution(elements):
    all_set = set(elements[:])

    dp = [elements[0]]
    double_elements = elements * 2

    for i in range(1, len(double_elements)):
        dp.append(dp[i - 1] + double_elements[i])

    for length in range(2, len(elements)):
        all_set.add(dp[length - 1])
        for j in range(length, length + len(elements) - 1):
            all_set.add(dp[j] - dp[j - length])

    all_set.add(dp[len(elements) - 1])
    answer = len(all_set)
    return answer