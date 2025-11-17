class Solution:
    def kLengthApart(self, nums: list[int], k: int) -> bool:
        spaces = k
        for x in nums:
            if x == 1:
                if spaces < k:
                    return False
                spaces = 0
            else:
                spaces += 1
        return True


solution = Solution()
assert solution.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1], 2) == True
assert solution.kLengthApart([1, 0, 0, 1, 0, 1], 2) == False
assert solution.kLengthApart([1, 1, 1, 0], 3) == False
assert solution.kLengthApart([1, 0, 0, 0, 1, 0, 0, 1, 0], 2) == True
assert solution.kLengthApart([1, 0, 1], 2) == False
