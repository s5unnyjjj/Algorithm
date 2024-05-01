
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/150368
# 코드 설명: https://s5unnyjjj.tistory.com/105

def solution(users, emoticons):
    answer = []
    all_discounts = [10, 20, 30, 40]
    cand_discounts = []

    def dfs(ary_discnts, depth):
        if len(emoticons) == depth:
            cand_discounts.append(ary_discnts[:])
        else:
            for discount in all_discounts:
                ary_discnts[depth] = discount
                dfs(ary_discnts, depth + 1)
                ary_discnts[depth] = 0

    dfs([0] * len(emoticons), 0)

    for cur_discount in cand_discounts:
        cur_emoticons = [price * (1 - discount * 0.01) for price, discount in zip(emoticons, cur_discount)]
        cur_answer = [0, 0]
        for user in users:
            user_discount, user_max_price = user
            user_total = 0
            for i, per_discount in enumerate(cur_discount):
                if user_discount <= per_discount:
                    user_total += cur_emoticons[i]
            if user_max_price <= user_total:
                cur_answer[0] += 1
            else:
                cur_answer[1] += user_total
        if sum(answer) == 0:
            answer = cur_answer
        else:
            if answer[0] == cur_answer[0]:
                if answer[1] < cur_answer[1]:
                    answer = cur_answer
            elif answer[0] < cur_answer[0]:
                answer = cur_answer

    return answer