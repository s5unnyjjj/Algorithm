
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/172928

def solution(park, routes):
    height, width = len(park), len(park[0])

    directions = {'E':[0, 1], 'W':[0, -1], 'N':[-1, 0], 'S':[1, 0]}
    pos = [[x, y] for x in range(height) for y in range(width) if park[x][y] == 'S'][0]

    for route in routes:
        direct, step = route.split(' ')
        step = int(step)
        next_pos = pos.copy()
        for i in range(step):
            next_pos = [next_pos[0] + directions[direct][0], next_pos[1] + directions[direct][1]]
            if next_pos[0] < 0 or next_pos[0] >= height or next_pos[1] < 0 or next_pos[1] >= width:
                break
            if park[next_pos[0]][next_pos[1]] == 'X':
                break
            if i == step-1:
                pos = next_pos.copy()
                break
    return pos
