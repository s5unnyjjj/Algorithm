
# 문제 링크: https://leetcode.com/problems/daily-temperatures/description/

"""
Try #1 - RESULT: FAIL, REASON: Time Limit Exceeded
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stacks = [[temperatures[0], 0]]
        answer = [0] * len(temperatures)

        for temp_idx in range(1, len(temperatures)):
            rmv = []
            for st_idx in range(len(stacks)):
                if stacks[st_idx][0] < temperatures[temp_idx]:
                    answer[stacks[st_idx][1]] = temp_idx - stacks[st_idx][1]
                    rmv.append(stacks[st_idx])
            for rmv_value in rmv:
                stacks.remove(rmv_value)
            stacks.append([temperatures[temp_idx], temp_idx])
        return answer

"""
Try #2 - RESULT: SUCCESS
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stacks = []
        answer = [0] * len(temperatures)

        for idx, value in enumerate(temperatures):
            while stacks and value > temperatures[stacks[-1]]:
                tmp = stacks.pop()
                answer[tmp] = idx - tmp
            stacks.append(idx)
        return answer