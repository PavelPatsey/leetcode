class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        non_dec = None
        c = 0
        while not non_dec:
            non_dec = True
            min_sum = float("inf")
            j = None
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    non_dec = False
                pair_sum = nums[i] + nums[i + 1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    j = i
            if not non_dec:
                nums[j : j + 2] = [min_sum]
                c += 1
        return c


solution = Solution()
assert solution.minimumPairRemoval([5, 2, 3, 1]) == 2
assert solution.minimumPairRemoval([1, 2, 2]) == 0
