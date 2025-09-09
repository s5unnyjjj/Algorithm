
# 문제 링크: https://www.acmicpc.net/problem/1924

import sys

input = sys.stdin.readline

dates = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
month, date = map(int, input().split())

period = 0
if month != 1:
    period += sum(dates[:month-1])
period += date
print(days[period%7])



