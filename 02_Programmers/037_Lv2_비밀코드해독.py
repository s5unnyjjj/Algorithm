
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons
# 코드 설명: https://s5unnyjjj.tistory.com/121

"""
성공
"""
import itertools

answer = []
MAX_NUM = 5

def dfs(pos, impos, n, q, ans):
    global answer

    if not ans:
        if len(list(pos)) == MAX_NUM:
            answer.append(pos)
        else:
            total_number = set([i for i in range(1, n + 1)])
            res_pos = total_number - impos
            need_num = 5 - len(list(pos))
            if len(res_pos) >= need_num and need_num > 0 and len(res_pos) > 0:
                all_combi_res = itertools.combinations(list(res_pos), need_num)
                for combi_res in all_combi_res:
                    if len(pos | set(combi_res)) == MAX_NUM:
                        answer.append(pos | set(combi_res))

        return

    for i, (part_q, part_ans) in enumerate(zip(q, ans)):
        all_combi_pos = itertools.combinations(part_q, part_ans)
        for combi_pos in all_combi_pos:
            set_combi_pos = set(combi_pos)
            if set_combi_pos & impos:
                continue
            else:
                impos_in_partq = [x for x in part_q if x not in set_combi_pos]
                if set(impos_in_partq) & pos:
                    continue
                dfs(pos | set_combi_pos, impos | set(impos_in_partq), n, q[i + 1:], ans[i + 1:])
        return

def solution(n, q, ans):
    dfs(set(), set(), n, q, ans)

    return len(answer)

"""
실패: 테스트 케이스 7, 11에서 런타임에러 발생
"""
import itertools

answer = []
MAX_NUM = 5

def dfs(pos, impos, n, q, ans):
    global answer

    if not ans:
        if len(list(pos)) == MAX_NUM:
            answer.append(pos)
        else:
            total_number = set([i for i in range(1, n + 1)])
            res_pos = total_number - impos
            need_num = 5 - len(list(pos))
            # if len(res_pos) >= need_num and need_num > 0 and len(res_pos) > 0:
            all_combi_res = itertools.combinations(list(res_pos), need_num)
            for combi_res in all_combi_res:
                if len(pos | set(combi_res)) == MAX_NUM:
                    answer.append(pos | set(combi_res))

        return

    for i, (part_q, part_ans) in enumerate(zip(q, ans)):
        all_combi_pos = itertools.combinations(part_q, part_ans)
        for combi_pos in all_combi_pos:
            set_combi_pos = set(combi_pos)
            if set_combi_pos & impos:
                continue
            else:
                impos_in_partq = [x for x in part_q if x not in set_combi_pos]
                if set(impos_in_partq) & pos:
                    continue
                dfs(pos | set_combi_pos, impos | set(impos_in_partq), n, q[i + 1:], ans[i + 1:])
        return

def solution(n, q, ans):
    dfs(set(), set(), n, q, ans)

    return len(answer)