

# 문제 링크: https://leetcode.com/problems/remove-duplicate-letters/description/

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counters = collections.Counter(s)
        seen = set()
        stacks = []

        for char in s:
            counters[char] -= 1
            if char in seen:
                continue
            while stacks and char < stacks[-1] and counters[stacks[-1]] > 0:
                seen.remove(stacks.pop())
            stacks.append(char)
            seen.add(char)

        return ''.join(stacks)