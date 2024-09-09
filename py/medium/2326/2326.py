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


def _get_list_node(head: List) -> ListNode:
    node = current_node = ListNode(head[0])
    for value in head[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next
    return node


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        pass


solution = Solution()

test_head = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
list_node = _get_list_node(test_head)
assert list_node.traversal() == test_head
