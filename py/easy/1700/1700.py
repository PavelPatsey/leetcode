from typing import List
from collections import deque


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_deque = deque(students)
        sandwiches_deque = deque(sandwiches)

        def recursion():
            if not sandwiches_deque:
                return []
            if sandwiches_deque[0] not in students_deque:
                return students_deque
            if students_deque[0] == sandwiches_deque[0]:
                students_deque.popleft()
                sandwiches_deque.popleft()
                return recursion()
            students_deque.append(students_deque.popleft())
            return recursion()

        return len(recursion())


solution = Solution()
assert solution.countStudents([1], [1]) == 0
assert solution.countStudents([1], [0]) == 1
assert solution.countStudents([1, 1, 0, 0], [0, 1, 0, 1]) == 0
assert solution.countStudents([1, 1, 1, 0, 0, 1], [1, 0, 0, 0, 1, 1]) == 3
