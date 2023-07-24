# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        for brackets in s:
            if brackets in mapping:
                if not stack or mapping[brackets] != stack.pop():
                    return False
            else:
                stack.append(brackets)
        return not stack


"""
s = "([{}])"
sol = Solution()
result = sol.isValid(s)
print(f"Input string: {s}")
print(f"Is valid: {result}")
"""