class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        nums_set = set()
        for x in nums:
            if x > k:
                nums_set.add(x)
            elif x < k:
                return -1
        return len(nums_set)


solution = Solution()
assert solution.minOperations([1], 1) == 0
assert solution.minOperations([2, 1, 2], 2) == -1
assert solution.minOperations([5, 2, 5, 4, 5], 2) == 2
assert solution.minOperations([9, 7, 5, 3], 1) == 4
