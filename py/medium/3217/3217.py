from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traversal(self):
        result = []
        node = self
        while node:
            result.append(node.val)
            node = node.next
        return result


class Solution:
    def modifiedList(
        self,
        nums: List[int],
        head: Optional[ListNode],
    ) -> Optional[ListNode]:
        nums_set = set(nums)
        node = head
        while node and node.val in nums_set:
            node = node.next

        if not node:
            return None

        previous = node
        current = node.next
        while current:
            if current.val not in nums_set:
                previous.next = current
                previous = current
            current = current.next
        previous.next = None
        return node


test_head = [1, 2, 1, 2, 1, 2]
list_node = ListNode(1)
list_node.next = ListNode(2)
list_node.next.next = ListNode(1)
list_node.next.next.next = ListNode(2)
list_node.next.next.next.next = ListNode(1)
list_node.next.next.next.next.next = ListNode(2)

list_node_2 = ListNode(2)
list_node_2.next = ListNode(2)
list_node_2.next.next = ListNode(2)

solution = Solution()
a = solution.modifiedList([1], list_node)

assert solution.modifiedList([1], list_node).traversal() == list_node_2.traversal()
