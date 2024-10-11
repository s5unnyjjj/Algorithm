
# 문제 링크: https://leetcode.com/problems/add-two-numbers/description/
# 코드 설명: https://s5unnyjjj.tistory.com/120

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reverse_l1 = self.reverse(l1)
        final_l1 = self.changeList(reverse_l1)

        reverse_l2 = self.reverse(l2)
        final_l2 = self.changeList(reverse_l2)

        ans = int(''.join(str(e) for e in final_l1)) + int(''.join(str(e) for e in final_l2))

        return self.changeLikednode(str(ans))

    def reverse(self, head):
        node, prev = head, None

        while node is not None:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev

    def changeList(self, head):
        node = head
        ary = []

        while node is not None:
            ary.append(node.val)
            node = node.next

        return ary

    def changeLikednode(self, contents):
        head = None

        # Check additional explanation below
        for content in contents:
            node = ListNode(content)  # Step1
            node.next = head  # Step2
            head = node  # Step3

        return node