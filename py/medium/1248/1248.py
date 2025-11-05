class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        converted = [x % 2 for x in nums]
        print(f"{converted=}")
        indexes = [i for i, x in enumerate(converted) if x == 1]
        res = 0
        print(f"{indexes=}")
        l = 0
        r = k - 1
        while r < len(indexes):
            if l == 0:
                before = indexes[0] + 1
            else:
                before = indexes[l] - indexes[l - 1]

            if r + 1 == len(indexes):
                after = len(converted) - indexes[r]
            else:
                after = indexes[r + 1] - indexes[r]
            dr = before * after
            res += dr
            l += 1
            r += 1
        return res


solution = Solution()
assert solution.numberOfSubarrays([1, 1, 2, 1, 1], 3) == 2
assert solution.numberOfSubarrays([2, 4, 6], 1) == 0
assert solution.numberOfSubarrays([2044, 96397, 50143], 1) == 3
assert solution.numberOfSubarrays([2, 2, 2, 1, 2, 2, 1, 2, 2, 2], 2) == 16
assert solution.numberOfSubarrays([1, 1, 1], 1) == 3
