from collections import Counter


class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        res = 0
        if numOperations == 0:
            counter = Counter(nums)
            return max(counter.values())
        new_oper_nums = numOperations - 1
        for dn in range(-k, k + 1):
            for i in range(len(nums)):
                new_nums = nums[:]
                new_nums[i] += dn
                res = max(self.maxFrequency(new_nums, k, new_oper_nums), res)
        return res


n = 1
assert list(range(-n, n + 1)) == [-1, 0, 1]
n = 2
assert list(range(-n, n + 1)) == [-2, -1, 0, 1, 2]
n = 0
assert list(range(-n, n + 1)) == [0]

solution = Solution()
assert solution.maxFrequency([1, 4, 5], 1, 2) == 2
assert solution.maxFrequency([5, 11, 20, 20], 5, 1) == 2
assert solution.maxFrequency([13, 37, 37], 30, 3) == 3
