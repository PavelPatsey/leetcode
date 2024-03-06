from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        has_cycle = False
        while fast and fast.next and not has_cycle:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                has_cycle = True

        return has_cycle


head = [3, 2, 0, -4]
pos = 1
list_node = ListNode(3)
list_node.next = ListNode(2)
list_node.next.next = ListNode(0)
list_node.next.next.next = ListNode(-4)
list_node.next.next.next.next = list_node.next

solution = Solution()
assert solution.hasCycle(list_node) is True
