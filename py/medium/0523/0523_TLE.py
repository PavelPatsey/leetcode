class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        return check_subarray_sum(0, len(nums) - 1, sum(nums), nums, k)


def check_subarray_sum(l: int, r: int, cur_sum: int, nums: list[int], k: int) -> bool:
    if l >= r:
        return False
    if cur_sum % k == 0:
        return True
    a = check_subarray_sum(l + 1, r, cur_sum - nums[l], nums, k)
    b = check_subarray_sum(l, r - 1, cur_sum - nums[r], nums, k)
    c = check_subarray_sum(l + 1, r - 1, cur_sum - nums[l] - nums[r], nums, k)
    return any((a, b, c))


solution = Solution()
assert solution.checkSubarraySum([23, 2, 4, 6, 7], 6) == True
assert solution.checkSubarraySum([23, 2, 6, 4, 7], 6) == True
assert solution.checkSubarraySum([23, 2, 6, 4, 7], 13) == False
