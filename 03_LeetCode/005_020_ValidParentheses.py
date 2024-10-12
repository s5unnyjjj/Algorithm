
# 문제 링크: https://leetcode.com/problems/valid-parentheses/description/

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {'(' : ')', '[' : ']', '{':'}'}
        stack = []

        if len(s) < 2:
            return False
        else:
            for bracket in s:
                for pair in pairs:
                    if bracket == pair:
                        stack.append(pairs[pair])
                        break
                else:
                    if len(stack) == 0:
                        return False
                    elif bracket == stack.pop():
                        continue
                    else:
                        return False
            return len(stack) == 0