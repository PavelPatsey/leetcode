from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def _traversal(node: ListNode):
        result = []
        while node.next:
            result.append(node.val)
            node = node.next
        return result

    def modifiedList(
            self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        pass


# head = [1,2,3,4,5]
list_node = ListNode(1)
list_node.next = ListNode(2)
list_node.next.next = ListNode(3)
list_node.next.next.next = ListNode(4)
list_node.next.next.next.next = ListNode(5)

solution = Solution()
solution._traversal(list_node) == [1, 2, 3, 4, 5]
# assert solution.modifiedList([1, 2, 3], list_node) == [2, 2, 2]
