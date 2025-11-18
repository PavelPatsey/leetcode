class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        last = None
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                last = 2
                i += 2
            else:
                last = 1
                i += 1
        return last == 1


s = Solution()
assert s.isOneBitCharacter([1, 0, 0]) == True
assert s.isOneBitCharacter([1, 1, 1, 0]) == False
