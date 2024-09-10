
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340212
# 코드 설명: https://s5unnyjjj.tistory.com/115

"""
Try #1 - RESULT: FAIL
"""
def solution(diffs, times, limit):
    right_level, left_level = min(diffs), max(diffs)
    max_level = left_level
    answers = max_level + 1

    while right_level < left_level:
        cur_level = (right_level + left_level) // 2
        if answers != max_level + 1 and cur_level == answers:
            break

        myTime = 0
        time_prev = 0
        for diff, time_cur in zip(diffs, times):
            if diff <= cur_level:
                myTime += time_cur
            else:
                n = diff - cur_level
                total_time = time_cur + time_prev
                myTime += n * total_time + time_cur
            time_prev = time_cur

        if myTime <= limit:
            answers = min(answers, cur_level)

        if myTime > limit:
            right_level = cur_level
        else:
            left_level = cur_level + 1

    return answers


"""
Try #2 - RESULT: FAIL
"""
def solution(diffs, times, limit):
    right_level, left_level = min(diffs), max(diffs)
    max_level = left_level
    answers = max_level + 1

    while right_level < left_level:
        cur_level = (right_level + left_level) // 2
        if answers != max_level + 1 and cur_level == answers:
            break

        myTime = 0
        time_prev = 0
        for diff, time_cur in zip(diffs, times):
            if diff <= cur_level:
                myTime += time_cur
            else:
                n = diff - cur_level
                total_time = time_cur + time_prev
                myTime += n * total_time + time_cur
            time_prev = time_cur
            if myTime > limit:
                break

        if myTime <= limit:
            answers = min(answers, cur_level)

        if myTime > limit:
            right_level = cur_level
        else:
            left_level = cur_level + 1

    return answers


"""
Try #3 - RESULT: SUCCESS
"""
def solution(diffs, times, limit):
    right_level, left_level = 0, 100001
    answers = 100002

    while right_level <= left_level:
        cur_level = (right_level + left_level) // 2
        if answers == cur_level:
            break

        myTime = 0
        time_prev = 0
        for diff, time_cur in zip(diffs, times):
            if diff <= cur_level:
                myTime += time_cur
            else:
                n = diff - cur_level
                total_time = time_cur + time_prev
                myTime += (n * total_time + time_cur)
            time_prev = time_cur
            if myTime >= limit:
                break

        if myTime <= limit:
            answers = min(answers, cur_level)

        if myTime > limit:
            right_level = cur_level
        else:
            left_level = cur_level + 1

    return answers
