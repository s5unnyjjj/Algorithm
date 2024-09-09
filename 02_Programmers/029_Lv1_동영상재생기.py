

# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/340213

def change_to_minute(times):
    hour, minute = times.split(':')
    return int(hour) * 60 + int(minute)

def change_to_origin(minute):
    hour, minute = str(minute//60), str(minute %60)
    if len(hour) == 1:
        hour = "0" + hour
    if len(minute) == 1:
        minute = "0" + minute
    return ":".join([hour, minute])


def solution(video_len, pos, op_start, op_end, commands):
    cur_time = change_to_minute(pos)
    end_time = change_to_minute(video_len)
    op_time = [change_to_minute(op_start), change_to_minute(op_end)]

    for command in commands:
        if op_time[0] <= cur_time <= op_time[1]:
            cur_time = op_time[1]

        if command == "prev":
            cur_time -= 10
            if cur_time < 0:
                cur_time = 0
        elif command == "next":
            cur_time += 10
            if cur_time > end_time:
                cur_time = end_time

    if op_time[0] <= cur_time <= op_time[1]:
        cur_time = op_time[1]
    return change_to_origin(cur_time)