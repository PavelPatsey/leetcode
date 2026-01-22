class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        non_dec = None
        c = 0
        while not non_dec and len(nums) > 1:
            non_dec = True
            s = nums[0] + nums[1]
            j = 0
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    non_dec = False
                if nums[i] + nums[i + 1] < s:
                    s = nums[i] + nums[i + 1]
                    j = i
            if non_dec:
                return c
            nums[j : j + 2] = [s]
            c += 1
        return c


solution = Solution()
assert solution.minimumPairRemoval([5, 2, 3, 1]) == 2
assert solution.minimumPairRemoval([1, 2, 2]) == 0
