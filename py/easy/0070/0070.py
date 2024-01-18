from functools import cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def _climb_stairs(n):
            if n <= 2:
                return n
            return _climb_stairs(n - 1) + _climb_stairs(n - 2)

        return _climb_stairs(n)


solution = Solution()
assert solution.climbStairs(1) == 1
assert solution.climbStairs(2) == 2
assert solution.climbStairs(3) == 3
assert solution.climbStairs(4) == 5
