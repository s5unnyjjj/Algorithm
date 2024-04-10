
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/67257
# 코드 설명: https://s5unnyjjj.tistory.com/85

import re
from itertools import permutations


def calculation(n1, n2, operation):
    if operation == '-':
        return n1 - n2
    elif operation == '*':
        return n1 * n2
    elif operation == '+':
        return n1 + n2


def solution(expression):
    answer = 0

    operations = list(filter(None, re.split('[0-9]', expression)))

    for opt_operations in list(permutations(list(set(operations)), len(list(set(operations))))):
        numbers = list(map(int, re.split('[+,*,-]', expression)))
        operations = list(filter(None, re.split('[0-9]', expression)))
        for opt_operation in opt_operations:
            while True:
                if not opt_operation in operations:
                    break
                for i, operation in enumerate(operations):
                    if opt_operation == operation:
                        tmp = calculation(numbers[i], numbers[i + 1], operation)
                        del operations[i]
                        numbers = numbers[:i] + [tmp] + numbers[i + 2:]
                        break
        tmp = abs(numbers[0])

        if answer <= tmp:
            answer = tmp

    return answer