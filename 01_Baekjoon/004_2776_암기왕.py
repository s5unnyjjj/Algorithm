
# 문제 링크: https://www.acmicpc.net/problem/2776
# 코드 설명: https://s5unnyjjj.tistory.com/94

import sys
input = sys.stdin.readline

T = int(input())

def binary_search(arr, tgt):
    left, right = 0, len(arr)-1
    flag = False
    while left <= right:
        mid = (left+right) // 2

        if arr[mid] < tgt:
            left = mid + 1
        elif arr[mid] > tgt:
            right = mid-1
        else:
            flag = True
            break
    return flag


for _ in range(T):
    N = int(input())
    N_list = sorted(list(map(int, input().split())))
    M = int(input())
    M_list = list(map(int, input().split()))

    for M_value in M_list:
        if binary_search(N_list, M_value):
            print('1')
        else:
            print('0')