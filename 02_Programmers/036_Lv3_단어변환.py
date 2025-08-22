
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/43163

answer = 51

def dfs(begin, target, words, step):
    global answer
    if begin == target:
        if answer > step:
            answer = step
        return

    for word in words:
        dif = 0
        for begin_char, char in zip(begin, word):
            if begin_char != char:
                if dif > 1:
                    break
                else:
                    dif += 1
        if dif == 1:
            words.remove(word)
            dfs(word, target, words, step + 1)
            words.append(word)

def solution(begin, target, words):
    dfs(begin, target, words, 0)

    if answer == 51:
        return 0

    return answer