
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    answer = []
    dates = []
    for progress, speed in zip(progresses, speeds):
        date = (100 - progress) // speed
        if (100 - progress) % speed != 0:
            date += 1
        dates.append(date)

    for i, date in enumerate(dates):
        if not answer:
            answer.append([date, 1])
        else:
            if answer[-1][0] < date:
                answer.append([date, 1])
            elif answer[-1][0] >= date:
                answer[-1] = [answer[-1][0], answer[-1][1] + 1]

    return [num for _, num in answer]