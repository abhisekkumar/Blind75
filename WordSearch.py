# https://leetcode.com/problems/word-search/description/
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True

        def dfs(board, word, i, j, k):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[k]:
                return False
            if k == len(word) - 1:
                return True
            temp, board[i][j] = board[i][j], '/'
            result = dfs(board, word, i + 1, j, k + 1) or \
                     dfs(board, word, i - 1, j, k + 1) or \
                     dfs(board, word, i, j + 1, k + 1) or \
                     dfs(board, word, i, j - 1, k + 1)
            board[i][j] = temp
            return result

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(board, word, i, j, 0):
                    return True
        return False


import unittest


class TestWordSearch(unittest.TestCase):

    def test_word_exists(self):
        solution = Solution()  # Create an instance of Solution class
        board = [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ]
        self.assertTrue(solution.exist(board, "ABCCED"))
        self.assertTrue(solution.exist(board, "SEE"))
        self.assertFalse(solution.exist(board, "ABCB"))

    def test_empty_word(self):
        solution = Solution()  # Create an instance of Solution class
        board = [
            ['A', 'B', 'C'],
            ['D', 'E', 'F'],
            ['G', 'H', 'I']
        ]
        self.assertTrue(solution.exist(board, ""))

    def test_word_longer_than_board(self):
        solution = Solution()  # Create an instance of Solution class
        board = [['A']]
        self.assertFalse(solution.exist(board, "AB"))

    # ... You can add more test cases ...


if __name__ == "__main__":
    unittest.main()

'''
i as row and j as column and k as the index of the word
board[i][j] == word[k] and dfs(board, word, i, j, k+1)

base case: 
i < 0 
i >= len(board)
j < 0
j >= len(board[0]) 
or board[i][j] != word[k]

  0 1 2 3
0 A B C E
1 S F C S
2 A D E E

target: A B C C E D

'''
