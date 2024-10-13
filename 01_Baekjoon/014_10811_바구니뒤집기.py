
# # 문제 링크: https://www.acmicpc.net/problem/10811

import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
basket = [i for i in range(1, N+1)]

for _ in range(M):
    start, end = list(map(int, input().split()))
    reverse_basket = basket[start-1:end]
    reverse_basket.reverse()
    basket = basket[:start-1] + reverse_basket + basket[end:]

print(' '.join(list(map(str, basket))))