
# 문제 링크: https://leetcode.com/problems/reverse-linked-list/description/
# 코드 설명: https://s5unnyjjj.tistory.com/112

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, None

        while node is not None:
            temp = node.next    # Step1
            node.next= prev     # Step2
            prev = node         # Step3
            node = temp         # Step4

        return prev