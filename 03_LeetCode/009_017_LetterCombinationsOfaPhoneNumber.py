
# 문제 링크: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        result = []

        def dfs(idx, path):
            """
            - dfs(v+1, path+vv)
                - v = 0, vv = “a”, “b”, “c” ⇒ dfs(1, vv)
                - v = 1, vv = “d”, “e”, “f” ⇒ dfs(2, vv)
                - [”ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf”]
            - dfs(idx+1, path+vv)
                - v = 0, vv = “a”, “b”, “c” ⇒ dfs(1, vv)
                - v = 1, vv = “d”, “e”, “f” ⇒ dfs(1, vv)
                - ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf", "dd", "de", "df", "ed", "ee", "ef", "fd", "fe", "ff"]
            """
            if len(path) == len(digits):
                result.append(path)
                return
            for v in range(idx, len(digits)):
                for vv in pairs[digits[v]]:
                    dfs(v+1, path+vv)
                    # dfs(idx+1, path+vv)

        pairs = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        dfs(0, "")

        return result

