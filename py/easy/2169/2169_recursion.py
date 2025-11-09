class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        return count_operations(num1, num2, 0)


def count_operations(num1: int, num2: int, counter: int) -> int:
    if num1 == 0 or num2 == 0:
        return counter
    if num1 >= num2:
        return count_operations(num1 - num2, num2, counter + 1)
    return count_operations(num1, num2 - num1, counter + 1)


solution = Solution()
assert solution.countOperations(2, 3) == 3
assert solution.countOperations(10, 10) == 1
