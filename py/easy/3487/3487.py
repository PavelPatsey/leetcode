class Solution:
    def maxSum(self, nums: list[int]) -> int:
        non_neg_nums = set()
        max_num = nums[0]
        for x in nums:
            if x > max_num:
                max_num = x
            if x > 0:
                non_neg_nums.add(x)
        return sum(non_neg_nums) if non_neg_nums else max_num


solution = Solution()
assert solution.maxSum([1, 2, 3, 4, 5]) == 15
assert solution.maxSum([1, 1, 0, 1, 1]) == 1
assert solution.maxSum([1, 2, -1, -2, 1, 0, -1]) == 3
