import heapq


class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        res = 0
        data = [-x for x in happiness]
        heapq.heapify(data)
        b = 0
        while k - b > 0:
            a = -heapq.heappop(data) - b
            if a <= 0:
                break
            res += a
            b += 1
        return res


solution = Solution()
assert solution.maximumHappinessSum([1, 2, 3], 2) == 4
assert solution.maximumHappinessSum([1, 1, 1, 1], 2) == 1
assert solution.maximumHappinessSum([2, 3, 4, 5], 1) == 5
assert solution.maximumHappinessSum([12, 1, 42], 3) == 53
