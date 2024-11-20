from typing import Dict


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def updated_counter(counter: Dict, char) -> Dict:
            c = {key: value for key, value in counter.items()}
            c[char] += 1
            return c

        def dfs(string, counter: Dict, number: int):
            if all(value >= k for value in counter.values()):
                return number
            if not string:
                return float("+inf")
            N = len(string)
            # print(f"{string=}, {counter=}, {number=}, {N=}")
            return min(
                dfs(
                    string[1:N],
                    updated_counter(counter, string[0]),
                    number + 1,
                ),
                dfs(
                    string[0 : N - 1],
                    updated_counter(counter, string[N - 1]),
                    number + 1,
                ),
            )

        res = dfs(s, {"a": 0, "b": 0, "c": 0}, 0)
        # print(f"{res=}")
        return res if res != float("+inf") else -1


solution = Solution()
assert solution.takeCharacters("aabbcc", 2) == 6
assert solution.takeCharacters("aabaaaacaabc", 2) == 8
assert solution.takeCharacters("a", 1) == -1
assert solution.takeCharacters("a", 0) == 0
