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


def _convert_list(head: List) -> ListNode:
    node = current_node = ListNode(head[0])
    for value in head[1:]:
        current_node.next = ListNode(value)
        current_node = current_node.next
    return node


class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        current_node = head
        matrix = [[-1 for _ in range(n)] for _ in range(m)]
        seen_set = set()
        row, col = 0, 0
        dr, dc = 0, 1
        matrix[row][col] = current_node.val
        current_node = current_node.next
        seen_set.add((row, col))
        while len(seen_set) != m * n and current_node:
            new_row, new_col = row + dr, col + dc
            if (
                (new_row, new_col) in seen_set
                or new_row in {-1, m}
                or new_col in {-1, n}
            ):
                dr, dc = dc, -dr
            row, col = row + dr, col + dc
            matrix[row][col] = current_node.val
            current_node = current_node.next
            seen_set.add((row, col))
        return matrix


solution = Solution()

test_list = [3, 0, 2, 6, 8, 1, 7, 9, 4, 2, 5, 5, 0]
list_node = _convert_list(test_list)
assert list_node.traversal() == test_list

assert solution.spiralMatrix(3, 5, list_node) == [
    [3, 0, 2, 6, 8],
    [5, 0, -1, -1, 1],
    [5, 2, 4, 9, 7],
]


test_list = [0, 1, 2]
list_node = _convert_list(test_list)
assert list_node.traversal() == test_list

assert solution.spiralMatrix(1, 4, list_node) == [[0, 1, 2, -1]]
