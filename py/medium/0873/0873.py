from typing import List


class Solution:
    @staticmethod
    def is_valid(nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        elif nums[-3] + nums[-2] == nums[-1]:
            return True
        return False

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        sub_seqs = []
        for x in arr:
            for seq in sub_seqs:
                if self.is_valid(seq + [x]):
                    sub_seqs.append(seq + [x])
            sub_seqs.append([x])
        max_len = max(map(len, sub_seqs))
        return max_len if max_len >= 3 else 0


solution = Solution()
assert solution.lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]) == 5
assert solution.lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]) == 3
assert solution.lenLongestFibSubseq([2, 4, 7, 8, 9, 10, 14, 15, 18, 23, 32, 50]) == 5
