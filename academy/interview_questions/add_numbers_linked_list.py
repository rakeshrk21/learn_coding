from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        current = head
        d = 0
        while l1 is not None or l2 is not None or d is not None:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            result = l1val + l2val + d

            d = result / 10
            r = result % 10

            newNode = ListNode(r)
            current.next = newNode
            current = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return head.next


if __name__ == "__main__":


    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    print(Solution().addTwoNumbers(l1, l2))
