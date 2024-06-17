
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/135807

def gcd(a, b):
    if a % b == 0:
        return b
    return gcd(b, a % b)


def solution(arrayA, arrayB):
    answer = 0

    if len(arrayA) >= 2:
        gcdA = gcd(arrayA[0], arrayA[1])
        for valueA in arrayA[2:]:
            gcdA = gcd(gcdA, valueA)
    else:
        gcdA = arrayA[0]

    if len(arrayB) >= 2:
        gcdB = gcd(arrayB[0], arrayB[1])
        for valueB in arrayB[2:]:
            gcdB = gcd(gcdB, valueB)
    else:
        gcdB = arrayB[0]

    for valueA in arrayA:
        if valueA % gcdB == 0:
            break
    else:
        answer = max(answer, gcdB)

    for valueB in arrayB:
        if valueB % gcdA == 0:
            break
    else:
        answer = max(answer, gcdA)

    return answer