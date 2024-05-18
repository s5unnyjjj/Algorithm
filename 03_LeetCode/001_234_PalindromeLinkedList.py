
# 문제 링크: https://leetcode.com/problems/palindrome-linked-list/
# 코드 설명: https://s5unnyjjj.tistory.com/manage/posts/

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_ary = []
        cur_node = head

        # Check additional explanation below
        while cur_node is not None:
            list_ary.append(cur_node.val)
            cur_node = cur_node.next

        if list_ary is None:
            return True

        n = len(list_ary)
        for i in range(int(n / 2)):
            if list_ary[i] == list_ary[n - i - 1]:
                continue
            else:
                return False
        return True