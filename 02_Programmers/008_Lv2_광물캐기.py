
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/172927#
# 코드 설명: https://s5unnyjjj.tistory.com/101

mins = {'diamond': 0, 'iron': 1, 'stone': 2}
tired = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]
answer = []


def calc_minerals(i, minerals):
    cur_total = 0
    cnt = 0
    for mineral in minerals:
        cur_total += tired[i][mins[mineral]]
        cnt += 1
        if cnt == 5:
            break
    return cnt, cur_total


def dfs(picks, minerals, total):
    if answer:
        if answer[-1] < total:
            return
    if sum(picks) == 0:
        answer.append(total)
        return
    for i, pick in enumerate(picks):
        if picks[i] == 0:
            continue
        else:
            picks[i] -= 1
            cnt, cur_total = calc_minerals(i, minerals)
            if cnt == 5:
                dfs(picks, minerals[5:], total + cur_total)
                picks[i] += 1
            else:
                answer.append(total + cur_total)
                picks[i] += 1
                return


def solution(picks, minerals):
    for i in range(3):
        if picks[i] > 0:
            picks[i] -= 1
            cnt, cur_total = calc_minerals(i, minerals)
            if cnt == 5:
                dfs(picks, minerals[5:], cur_total)
                picks[i] += 1
            else:
                answer.append(total + cur_total)

    return min(answer)