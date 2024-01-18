class Solution:
    def climbStairs(self, n: int) -> int:
        def _climb_stairs(n, step, a, b):
            if n == step:
                return a + b
            return _climb_stairs(n, step + 1, b, a + b)

        return _climb_stairs(n, 1, 0, 1)


solution = Solution()
assert solution.climbStairs(1) == 1
assert solution.climbStairs(2) == 2
assert solution.climbStairs(3) == 3
assert solution.climbStairs(4) == 5
