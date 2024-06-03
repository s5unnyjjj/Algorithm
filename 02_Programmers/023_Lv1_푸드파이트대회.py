
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/134240

def solution(food):
    answer = ''
    for i, food_num in enumerate(food):
        if i == 0:
            continue
        final_food_num = food_num // 2
        answer += str(i)*final_food_num
    answer += ('0'+answer[::-1])
    return answer