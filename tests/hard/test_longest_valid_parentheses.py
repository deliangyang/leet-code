import unittest
from src.hard.longest_valid_parentheses import Solution


class MyTestCase(unittest.TestCase):
    def test_longest_valid_parentheses(self):
        solution = Solution()
        self.assertEqual(4, solution.longestValidParentheses(')()())'))
        self.assertEqual(6, solution.longestValidParentheses('(()())'))
        self.assertEqual(2, solution.longestValidParentheses('(()'))
        self.assertEqual(4, solution.longestValidParentheses('(())'))

