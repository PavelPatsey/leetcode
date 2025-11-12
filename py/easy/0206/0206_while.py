class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def travers(self) -> list:
        res = []
        node = self
        while node:
            res.append(node.val)
            node = node.next
        return res


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        current = head
        next_node = head.next
        head.next = None
        while next_node:
            prev = current
            current = next_node
            next_node = current.next
            current.next = prev
        return current


solution = Solution()

node5 = ListNode(5)
node4 = ListNode(4, node5)
node3 = ListNode(3, node4)
node2 = ListNode(2, node3)
original_head = ListNode(1, node2)


node1 = ListNode(1)
node2 = ListNode(2, node1)
node3 = ListNode(3, node2)
node4 = ListNode(4, node3)
reversed_head = ListNode(5, node4)

assert original_head.travers() == [1, 2, 3, 4, 5]
assert reversed_head.travers() == [5, 4, 3, 2, 1]
expected_reversed_head = solution.reverseList(original_head)
assert reversed_head.travers() == expected_reversed_head.travers()
