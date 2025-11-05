class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        converted = (x % 2 for x in nums)
        indexes = [i for i, x in enumerate(converted) if x == 1]
        res = 0
        l = 0
        r = k - 1
        while r < len(indexes):
            if l == 0:
                left_variants_count = indexes[0] + 1
            else:
                left_variants_count = indexes[l] - indexes[l - 1]

            if r + 1 == len(indexes):
                right_variants_count = len(nums) - indexes[r]
            else:
                right_variants_count = indexes[r + 1] - indexes[r]
            res += left_variants_count * right_variants_count
            l += 1
            r += 1
        return res


solution = Solution()
assert solution.numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
assert solution.numberOfSubarrays([2, 4, 6], 1) == 0
assert solution.numberOfSubarrays([2044, 96397, 50143], 1) == 3
assert solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16
assert solution.numberOfSubarrays([1, 1, 1], 1) == 3
