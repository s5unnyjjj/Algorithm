
# 문제 링크: https://leetcode.com/problems/merge-two-sorted-lists/
# 코드 설명: https://s5unnyjjj.tistory.com/111


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_node = ListNode(0)

        cur_node = new_node

        while list1 and list2:
            if list1.val <= list2.val:
                cur_node.next = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                list2 = list2.next

            cur_node = cur_node.next

        if list1 is not None:
            cur_node.next = list1
        if list2 is not None:
            cur_node.next = list2

        return new_node.next