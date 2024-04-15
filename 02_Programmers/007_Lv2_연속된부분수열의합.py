
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/178870
# 코드 설명: https://s5unnyjjj.tistory.com/100


def solution(sequence, k):
    answer = []
    start_idx = 0
    cur_summation = sequence[start_idx]
    if cur_summation == k:
        return [start_idx, start_idx]
    for end_idx in range(1, len(sequence)):
        cur_summation += sequence[end_idx]
        while True:
            if cur_summation < k:
                break
            elif cur_summation == k:
                answer.append([start_idx, end_idx -start_idx +1, end_idx])
                break
            else:
                cur_summation -= sequence[start_idx]
                start_idx += 1

    answer.sort(key=lambda x :x[1])
    return [answer[0][0], answer[0][2]]