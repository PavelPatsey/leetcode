class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        d = {"0": 1, "10": 2, "11": 2}
        code = ""
        last_char = None
        for b in bits:
            code = code + str(b)
            if code in d:
                last_char = d[code]
                code = ""
        return last_char == 1


s = Solution()
assert s.isOneBitCharacter([1, 0, 0]) == True
assert s.isOneBitCharacter([1, 1, 1, 0]) == False
