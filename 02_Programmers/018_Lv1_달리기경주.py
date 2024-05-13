
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/178871
# 코드 설명: https://s5unnyjjj.tistory.com/108

"""
성공
"""
def solution(players, callings):
    players_dict = {}

    for i, player in enumerate(players):
        players_dict[player] = i

    for calling in callings:
        cur_i = players_dict[calling]

        players_dict[calling] = cur_i - 1
        players_dict[players[cur_i - 1]] = cur_i

        players[cur_i] = players[cur_i - 1]
        players[cur_i - 1] = calling

    return players

"""
실패: 시간 초과
"""
def solution(players, callings):
    for calling in callings:
        idx = players.index(calling)
        change_name = players[idx-1]
        players[idx-1] = calling
        players[idx] = change_name
    return players