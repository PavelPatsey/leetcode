class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        a, b = num1, num2
        counter = 0
        while a != 0 and b != 0:
            if a >= b:
                a = a - b
            else:
                b = b - a
            counter += 1
        return counter


solution = Solution()
assert solution.countOperations(2, 3) == 3
assert solution.countOperations(10, 10) == 1
