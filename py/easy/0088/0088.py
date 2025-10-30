class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lst = nums1[:m] + nums2
        lst.sort()
        for i in range(len(nums1)):
            nums1[i] = lst[i]


solution = Solution()

nums1 = [1, 2, 3, 0, 0, 0]
solution.merge(nums1=nums1, m=3, nums2=[2, 5, 6], n=3)
assert nums1 == [1, 2, 2, 3, 5, 6]

nums1 = [1]
solution.merge(nums1=nums1, m=1, nums2=[], n=0)
assert nums1 == [1]

nums1 = [0]
solution.merge(nums1=nums1, m=0, nums2=[1], n=1)
assert nums1 == [1]
