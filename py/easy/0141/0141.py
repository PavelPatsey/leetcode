from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        node = head
        has_cycle = False
        while node and not has_cycle:
            if node in visited:
                has_cycle = True
            visited.add(node)
            node = node.next
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
