from itertools import permutations


class Solution:
    @staticmethod
    def brute_force_next_permutation(nums: list[int]) -> list:
        sorted_permutations = sorted(list(x) for x in set(permutations(nums)))
        l = len(sorted_permutations)
        for i, x in enumerate(sorted_permutations):
            if x == nums:
                res = sorted_permutations[(i + 1) % l]
                print(f"{res=}")
                return res
        assert False

    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new_nums = self.brute_force_next_permutation(nums)
        for i in range(len(nums)):
            nums[i] = new_nums[i]


solution = Solution()
assert solution.brute_force_next_permutation([1, 2, 3]) == [1, 3, 2]
assert solution.brute_force_next_permutation([3, 2, 1]) == [1, 2, 3]
assert solution.brute_force_next_permutation([1, 1, 5]) == [1, 5, 1]
assert solution.brute_force_next_permutation([5, 4, 1, 3, 2]) == [5, 4, 2, 1, 3]

nums = [1, 2, 3]
solution.nextPermutation(nums)
assert nums == [1, 3, 2]

nums = [3, 2, 1]
solution.nextPermutation(nums)
assert nums == [1, 2, 3]

nums = [1, 1]
solution.nextPermutation(nums)
assert nums == [1, 1]
