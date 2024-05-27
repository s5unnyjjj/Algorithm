

# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    minXY, maxXY = [51, 51], [-1, -1]
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                if minXY[0] > i:
                    minXY[0] = i
                if minXY[1] > j:
                    minXY[1] = j
                if maxXY[0] < i:
                    maxXY[0] = i
                if maxXY[1] < j:
                    maxXY[1] = j

    return [minXY[0], minXY[1], maxXY[0] + 1, maxXY[1] + 1]