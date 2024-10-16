import heapq


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        string = ""
        chars = [
            (-a, "a"),
            (-b, "b"),
            (-c, "c"),
        ]
        heapq.heapify(chars)

        char = heapq.heappop(chars)
        char_number, char_name = char
        if char_number <= -2:
            n = 2
        elif char_number == -1:
            n = 1
        else:
            assert False, f"Error! {char_number=}"
        char_number += n
        string += char_name * n
        prev_char = (char_number, char_name)

        while chars[0][0] != 0:
            char = heapq.heappop(chars)
            char_number, char_name = char
            if char_number <= -2:
                n = 2
            elif char_number == -1:
                n = 1
            else:
                assert False, f"Error! {char_number=}"
            heapq.heappush(chars, prev_char)
            char_number += n
            string += char_name * n
            prev_char = (char_number, char_name)

        return string


solution = Solution()
assert solution.longestDiverseString(1, 1, 7) == "ccaccbcc"
assert solution.longestDiverseString(7, 1, 0) == "aabaa"
