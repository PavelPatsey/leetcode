from typing import List, Optional
import math


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


def _convert_list(head: List) -> ListNode:
    node = current_node = ListNode(head[0])
    for value in head[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next
    return node


class Solution:
    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current_node = head
        while current_node.next:
            next_node = current_node.next
            _gcd = math.gcd(current_node.val, next_node.val)
            gcd_node = ListNode(_gcd)
            current_node.next = gcd_node
            gcd_node.next = next_node
            current_node = next_node
        return head


solution = Solution()

test_list = [18, 6, 10, 3]
list_node = _convert_list(test_list)
assert list_node.traversal() == test_list

transformed = solution.insertGreatestCommonDivisors(list_node)
assert transformed.traversal() == [18, 6, 6, 2, 10, 1, 3]
