class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        total = 0
        remainders = {0: -1}
        for i, n in enumerate(nums):
            total += n
            r = total % k
            if r not in remainders:
                remainders[r] = i
            elif i - remainders[r] > 1:
                return True
        return False


solution = Solution()
assert solution.checkSubarraySum([23, 2, 4, 6, 7], 6) == True
assert solution.checkSubarraySum([23, 2, 6, 4, 7], 6) == True
assert solution.checkSubarraySum([23, 2, 6, 4, 7], 13) == False
assert solution.checkSubarraySum([23, 2, 4, 6, 6], 7) == True
assert solution.checkSubarraySum([1, 0], 2) == False
