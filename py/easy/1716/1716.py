class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = n // 7, n % 7
        sum_weeks = 28 * weeks + 7 * weeks * (weeks - 1) // 2
        sum_days = days * weeks + days * (days + 1) // 2
        return sum_weeks + sum_days


solution = Solution()
assert solution.totalMoney(4) == 10
assert solution.totalMoney(10) == 37
