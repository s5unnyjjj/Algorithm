
# 문제 링크: https://leetcode.com/problems/permutations/description/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        pr_nums = []

        def dfs(cur_nums):
            if len(cur_nums) == 0:
                result.append(pr_nums[:])
                return

            for v in cur_nums:
                next_nums = cur_nums[:]
                # next_nums = cur_nums
                next_nums.remove(v)
                pr_nums.append(v)
                dfs(next_nums)
                pr_nums.pop()

        dfs(nums)

        return result

"""
* Additional information
 1. Time Comparison of result
  - Method using DFS: 33ms
  - Method using permutations of itertools: 27ms
"""