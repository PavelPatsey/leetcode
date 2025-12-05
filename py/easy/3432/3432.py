class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        is_even = sum(nums) % 2 == 0
        return len(nums) - 1 if is_even else 0


s = Solution()
assert s.countPartitions([10, 10, 3, 7, 6]) == 4
assert s.countPartitions([1, 2, 2]) == 0
assert s.countPartitions([2, 4, 6, 8]) == 3
