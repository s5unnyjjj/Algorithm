
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons

MAX_MINUTE = 60

def arrange_time(time, add):
    hour, minute = time // 100, (time % 100) + add
    if minute >= MAX_MINUTE:
        minute -= MAX_MINUTE
        hour += 1
    return [hour, minute]


def solution(schedules, timelogs, startday):
    answer = 0

    days = [(i + startday) % 7 for i in range(7)]

    for ti, timelog in enumerate(timelogs):
        possible_hour, possible_minute = arrange_time(schedules[ti], 10)
        cnt = 0
        for day, time in enumerate(timelog):
            if days[day] in [0, 6]:
                cnt += 1
                continue
            cur_hour, cur_minute = arrange_time(time, 0)
            if possible_hour > cur_hour:
                cnt += 1
            elif possible_hour == cur_hour:
                if possible_minute >= cur_minute:
                    cnt += 1

        if cnt == 7:
            answer += 1
    return answer