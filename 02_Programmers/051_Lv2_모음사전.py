
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/84512

from itertools import product

def solution(word):
    final_answer = []
    alphabets = ['A', 'E', 'I', 'O', 'U']
    for i in range(len(alphabets)):
        words = list(product(alphabets, repeat=i + 1))
        final_answer.extend(''.join(word) for word in words)
    final_answer.sort()
    return final_answer.index(word) + 1


