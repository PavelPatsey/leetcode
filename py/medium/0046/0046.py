class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = make_permutations(nums)
        print(f"{res=}")
        return res


def make_permutations(nums: list[int]) -> list[list[int]]:
    res = []

    def _make_permutations(permutation: list[int], remaining: list):
        if len(permutation) == len(nums):
            res.append(permutation)
            return
        for i, x in enumerate(remaining):
            _make_permutations(permutation + [x], remaining[0:i] + remaining[i + 1 :])

    _make_permutations([], nums)
    return res


solution = Solution()
assert solution.permute([1, 2, 3]) == [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
]
