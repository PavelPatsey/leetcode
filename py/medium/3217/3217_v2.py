from typing import Self


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def traverse(self) -> list[int]:
        current = self
        res = []
        while current:
            res.append(current.val)
            current = current.next
        return res

    @classmethod
    def create_from_nums(cls, nums: list[int]) -> Self | None:
        """Create a linked list head from a list of numbers"""
        prev_node = None
        curr_node = None
        for x in reversed(nums):
            curr_node = ListNode(x, prev_node)
            prev_node = curr_node
        return curr_node


class Solution:
    def modifiedList(self, nums: list[int], head: ListNode | None) -> ListNode | None:
        nums_set = set(nums)
        new_head = head
        while new_head.val in nums:
            new_head = new_head.next

        if not new_head:
            return None

        current_node = new_head
        next_node = new_head.next
        while next_node:
            if next_node.val not in nums_set:
                current_node.next = next_node
                current_node = next_node
            next_node = next_node.next
        current_node.next = None
        return new_head


solution = Solution()

node2 = ListNode(2)
node1 = ListNode(1, node2)
assert node1.traverse() == [1, 2]

head = [1, 2, 3, 4, 5]
linked_head = ListNode.create_from_nums(head)
assert linked_head.traverse() == head
nums = [1, 2, 3]
modified_linked_head = ListNode.create_from_nums([4, 5])
assert (
    solution.modifiedList(nums, linked_head).traverse()
    == modified_linked_head.traverse()
)
