class Solution:
    def minOperations(self, nums: list[int]) -> int:
        res = min_operations(nums)
        return res


def min_operations(nums: list[int]) -> int:
    if sum(nums) == 0:
        return 0
    if 0 in nums:
        splitted_nums = split_by_zero(nums)
        return sum(min_operations(xs) for xs in splitted_nums)
    min_num = min(nums)
    new_nums = [0 if x == min_num else x for x in nums]
    return 1 + min_operations(new_nums)


def split_by_zero(nums: list[int]) -> list[int]:
    splitted = []
    current = []
    for i in range(len(nums)):
        if nums[i] != 0:
            current.append(nums[i])
        else:
            if current:
                splitted.append(current)
                current = []
    if current:
        splitted.append(current)
    return splitted


assert split_by_zero([0, 1, 2]) == [[1, 2]]
assert split_by_zero([0, 2]) == [[2]]
assert split_by_zero([2, 0]) == [[2]]
assert split_by_zero([0, 2, 0]) == [[2]]
assert split_by_zero([2]) == [[2]]
assert split_by_zero([1, 2, 1, 2, 1, 2]) == [[1, 2, 1, 2, 1, 2]]
assert split_by_zero([0, 2, 0, 2, 0, 2]) == [[2], [2], [2]]
assert split_by_zero([0, 2, 0, 2, 0, 2, 0]) == [[2], [2], [2]]

solution = Solution()
# leetcode tests
assert solution.minOperations([0, 2]) == 1
assert solution.minOperations([3, 1, 2, 1]) == 3
assert solution.minOperations([1, 2, 1, 2, 1, 2]) == 4
assert solution.minOperations([4, 3, 4, 6]) == 4

# my_tests
assert solution.minOperations([0]) == 0
assert solution.minOperations([1]) == 1
assert solution.minOperations([0, 0, 0]) == 0
assert solution.minOperations([0, 1, 2]) == 2
assert solution.minOperations([1, 1, 1, 2, 2, 2, 2, 9, 9, 2]) == 3
