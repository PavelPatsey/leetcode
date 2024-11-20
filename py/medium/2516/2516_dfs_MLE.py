from typing import Dict


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        def updated_counter(counter: Dict, char) -> Dict:
            c = {key: value for key, value in counter.items()}
            c[char] += 1
            return c

        visited = {}

        def dfs(left, right, counter: Dict, number: int):
            if (left, right) in visited:
                return visited[(left, right)]

            print(f"{left=}, {right=}, {counter=}, {number=}")
            if all(value >= k for value in counter.values()):
                return number
            if left > right:
                return float("+inf")
            a = dfs(left + 1, right, updated_counter(counter, s[left]), number + 1)
            b = dfs(left, right - 1, updated_counter(counter, s[right]), number + 1)
            visited[(left + 1, right)] = a
            visited[(left, right - 1)] = b
            return min(a, b)

        res = dfs(0, len(s) - 1, {"a": 0, "b": 0, "c": 0}, 0)
        print(f"{res=}")
        return res if res != float("+inf") else -1


solution = Solution()
assert solution.takeCharacters("aabbcc", 2) == 6
assert solution.takeCharacters("aabaaaacaabc", 2) == 8
assert solution.takeCharacters("a", 1) == -1
assert solution.takeCharacters("a", 0) == 0
