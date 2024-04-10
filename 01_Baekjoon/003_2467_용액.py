
# 문제 링크: https://www.acmicpc.net/problem/2467
# 코드 설명: https://s5unnyjjj.tistory.com/93

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

MIN_VALUE = -1000000001
MAX_VALUE = 1000000001
mem_arr = [n_list[0]]
answer = [[MIN_VALUE, n_list[0]], MAX_VALUE*2]

def binary_search(arr, tgt):
    left, right = 0, len(arr)-1

    while left < right:
        mid = (left+right) // 2
        if arr[mid] < tgt:
            left = mid + 1
        else:
            right = mid

    return right

for cur_n in n_list[1:]:
    if mem_arr[-1] < (cur_n*-1):
        dif = mem_arr[-1]+cur_n
        if abs(answer[1]) > abs(dif):
            answer = [[mem_arr[-1], cur_n], dif]
        mem_arr.append(cur_n)
    else:
        idx = binary_search(mem_arr, (cur_n*-1))
        next_n = 0
        left_n = mem_arr[idx-1]
        right_n = mem_arr[idx]
        if abs(left_n+cur_n) < abs(right_n+cur_n):
            dif = left_n + cur_n
            next_n = left_n
        else:
            dif = right_n + cur_n
            next_n = right_n
        if abs(answer[1]) > abs(dif):
            answer = [[next_n, cur_n], dif]
print(*answer[0])