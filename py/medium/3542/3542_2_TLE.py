from collections import deque


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        acc = 0
        splitted_nums = split_by_zero(nums)
        queue = deque(splitted_nums)
        while queue:
            cur_slice = queue.popleft()
            min_num = min(cur_slice)
            new_slice = [0 if x == min_num else x for x in cur_slice]
            acc += 1
            for lst in split_by_zero(new_slice):
                queue.append(lst)
        return acc


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
