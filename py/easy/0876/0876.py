from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


head = [1, 2, 3, 4, 5]
list_node = ListNode(1)
list_node.next = ListNode(2)
list_node.next.next = ListNode(3)
list_node.next.next.next = ListNode(4)
list_node.next.next.next.next = ListNode(5)

solution = Solution()
assert solution.middleNode(list_node) == list_node.next.next

list_node.next.next.next.next.next = ListNode(6)
assert solution.middleNode(list_node) == list_node.next.next.next
