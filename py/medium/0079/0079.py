from typing import List


class Solution:
    DIR_LIST = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        def _is_exist_dfs(visited, index, r, c):
            if word[index] != board[r][c]:
                return False

            if index == len(word) - 1:
                return True

            new_visited = visited.copy()
            new_visited.add((r, c))
            new_index = index + 1

            result = []
            for dr, dc in self.DIR_LIST:
                new_r, new_c = r + dr, c + dc
                if (
                    0 <= new_r < len_rows
                    and 0 <= new_c < len_cols
                    and board[new_r][new_c] == word[new_index]
                    and (new_r, new_c) not in visited
                ):
                    result.append(_is_exist_dfs(new_visited, new_index, new_r, new_c))
            return any(result)

        len_rows = len(board)
        len_cols = len(board[0])

        for row in range(len_rows):
            for col in range(len_cols):
                if _is_exist_dfs(set(), 0, row, col):
                    return True

        return False


solution = Solution()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCCED"
# assert solution.exist(board, word) is True
#
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "SEE"
# assert solution.exist(board, word) is True
#
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
# word = "ABCB"
# assert solution.exist(board, word) is False

board = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
word = "ABCESEEEFS"
word = "ABCESEEEFS"
assert solution.exist(board, word) is True
