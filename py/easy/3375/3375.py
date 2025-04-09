class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums_set = set(nums)
        result = 0
        for x in nums_set:
            if x > k:
                result += 1
            elif x < k:
                return -1
        return result


solution = Solution()
assert solution.minOperations([1], 1) == 0
assert solution.minOperations([2, 1, 2], 2) == -1
assert solution.minOperations([5, 2, 5, 4, 5], 2) == 2
assert solution.minOperations([9, 7, 5, 3], 1) == 4
