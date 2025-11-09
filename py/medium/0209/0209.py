class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        cur_sum = nums[0]
        left = right = 0
        min_len = float("inf")
        while right < len(nums) and left <= right:
            if cur_sum >= target:
                min_len = min(min_len, right - left + 1)
                cur_sum -= nums[left]
                left += 1
            elif right == len(nums) - 1:
                right += 1
            else:
                right += 1
                cur_sum += nums[right]
        return min_len if min_len < float("inf") else 0


solution = Solution()
assert solution.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]) == 2
assert solution.minSubArrayLen(4, [1, 4, 4]) == 1
assert solution.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]) == 0

assert solution.minSubArrayLen(11, [1]) == 0
assert solution.minSubArrayLen(11, [11]) == 1
