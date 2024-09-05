from typing import List


class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        sum_rolls_n = mean * (len(rolls) + n) - sum(rolls)
        rolls_n = [1] * n
        current_sum = sum(rolls_n)
        if sum_rolls_n > n * 6 or sum_rolls_n < n:
            return []
        x = sum_rolls_n - current_sum
        i = 0
        while x > 0:
            if x > 5:
                dx = 5
            else:
                dx = x
            x -= dx
            current_sum += dx
            rolls_n[i] += dx
            i += 1
        return rolls_n


solution = Solution()
assert sum(solution.missingRolls([3, 2, 4, 3], 4, 2)) == sum([6, 6])
assert len(solution.missingRolls([3, 2, 4, 3], 4, 2)) == len([6, 6])

assert sum(solution.missingRolls([1, 5, 6], 3, 4)) == sum([2, 3, 2, 2])
assert len(solution.missingRolls([1, 5, 6], 3, 4)) == len([2, 3, 2, 2])

assert sum(solution.missingRolls([1, 2, 3, 4], 6, 4)) == sum([])
assert len(solution.missingRolls([1, 2, 3, 4], 6, 4)) == len([])

assert sum(solution.missingRolls([6, 3, 4, 3, 5, 3], 1, 6)) == sum([])
assert len(solution.missingRolls([6, 3, 4, 3, 5, 3], 1, 6)) == len([])

assert sum(solution.missingRolls([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 1)) == sum([1])
assert len(solution.missingRolls([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1, 1)) == len([1])
