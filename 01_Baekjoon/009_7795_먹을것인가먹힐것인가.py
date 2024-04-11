
# 문제 링크: https://www.acmicpc.net/problem/7795


import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B = list(map(int, input().split()))
    A_array = sorted(list(map(int, input().split())))
    B_array = sorted(list(map(int, input().split())))
    total = 0
    for target in A_array:
        left, right = 0, len(B_array)-1
        res = -1
        while left <= right:
            mid = (left+right) // 2

            if B_array[mid] < target:
                res = mid
                left = mid + 1
            else:
                right = mid - 1
        total += (res+1)
    print(total)