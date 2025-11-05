class Solution:
    @staticmethod
    def is_nice(sub_nums: list[int], k: int) -> bool:
        return sum(True for x in sub_nums if x % 2 != 0) == k

    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if self.is_nice(nums[i : j + 1], k):
                    res += 1
        return res


solution = Solution()
assert solution.numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
assert solution.numberOfSubarrays([2, 4, 6], 1) == 0
assert solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16
assert solution.numberOfSubarrays([2044, 96397, 50143], 1) == 3
