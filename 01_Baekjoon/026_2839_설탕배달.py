
# 문제 링크: https://www.acmicpc.net/problem/2839

import sys

input = sys.stdin.readline

total_kg = int(input())
five_kg = total_kg // 5

for f_kg in range(five_kg, -1, -1):
    if (total_kg - (5*f_kg)) % 3 == 0:
        t_kg = (total_kg - (5*f_kg)) // 3
        print(f_kg+t_kg)
        exit(0)
print(-1)