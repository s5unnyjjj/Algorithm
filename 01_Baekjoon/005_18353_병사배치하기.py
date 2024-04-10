
# 문제 링크: https://www.acmicpc.net/problem/18353
# 코드 설명: https://s5unnyjjj.tistory.com/96

import sys
input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))


def binary_search(arr, tgt):
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left+right) // 2
        if arr[mid] > tgt:
            left = mid+1
        else:
            right = mid
    return right


MAX_VALUE = 10000001
lis_arr = [MAX_VALUE]

for num in n_list:
    if lis_arr[-1] > num:
        lis_arr.append(num)
    else:
        idx = binary_search(lis_arr, num)
        lis_arr[idx] = num

print(n-len(lis_arr)+1)