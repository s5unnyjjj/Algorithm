
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/132265
# 코드 설명: https://s5unnyjjj.tistory.com/107

"""
첫번째 시도 -> 실패
"""
def solution(topping):
    answer = []
    right, left = 0, len(topping) - 1

    while right < left:
        mid = (right + left) // 2
        rt = set(topping[:mid])
        lt = set(topping[mid:])

        if len(rt) == len(lt):
            if mid in answer:
                break
            else:
                answer.append(mid)
                if mid > len(topping)//2:
                    left = mid
                else:
                    right = mid + 1
        elif len(rt) < len(lt):
            right = mid + 1
        else:
            left = mid

    return len(answer)

"""
두번째 시도 -> 실패(시간초과)
"""
def solution(topping):
    right_num, left_num = [], []

    for idx, top in enumerate(topping):
        right_num.append(len(set(topping[:idx])))
        left_num.append(len(set(topping[idx:])))

    answer = [i for i in range(len(right_num)) if right_num[i] == left_num[i]]

    return len(answer)

"""
세번째 시도 -> 성공
"""
def solution(topping):
    right_num, left_num = [], []
    right_set, left_set = set(), set()

    for idx, top in enumerate(topping):
        right_set.add(top)
        right_num.append(len(right_set))

        left_set.add(topping[len(topping) - idx - 1])
        left_num.append(len(left_set))

    len_left = len(left_num)
    answer = [i for i in range(len(right_num) - 1) if right_num[i] == left_num[len_left - i - 2]]

    return len(answer)

"""
네번째 시도 -> 성공(세번째 시도보다 시간이 덜 소요됨)
"""
def solution(topping):
    right_num, left_num = [], []
    right_set, left_set = set(), set()

    for top in topping:
        right_set.add(top)
        right_num.append(len(right_set))

    for top in topping[::-1]:
        left_set.add(top)
        left_num.append(len(left_set))

    len_left = len(left_num)
    answer = [i for i in range(len(right_num) - 1) if right_num[i] == left_num[len_left - i - 2]]

    return len(answer)