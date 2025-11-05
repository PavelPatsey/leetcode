class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        odds = []
        counter = 0
        res = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] % 2 == 1:
                odds.append(r)
                counter += 1
            while counter > k and l < r:
                counter -= nums[l] % 2
                l += 1
            if k == counter:
                res += odds[-k] - l + 1
        return res


solution = Solution()
assert solution.numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
assert solution.numberOfSubarrays([2, 4, 6], 1) == 0
assert solution.numberOfSubarrays([2044, 96397, 50143], 1) == 3
assert solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16
assert solution.numberOfSubarrays([1, 1, 1], 1) == 3
