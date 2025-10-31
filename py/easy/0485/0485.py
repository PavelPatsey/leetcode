class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        counter = 0
        max_counter = 0
        for n in nums:
            if n == 1:
                counter += 1
            else:
                max_counter = max(max_counter, counter)
                counter = 0
        return max(max_counter, counter)


solution = Solution()
assert solution.findMaxConsecutiveOnes([1]) == 1
assert solution.findMaxConsecutiveOnes([0]) == 0
assert solution.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]) == 3
assert solution.findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]) == 2
