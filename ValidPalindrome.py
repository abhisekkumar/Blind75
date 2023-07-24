# https://leetcode.com/problems/valid-palindrome/
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and not self.isAlphaNumeric(s[l]):
                l += 1
            while r > l and not self.isAlphaNumeric(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1
        return True

    def isAlphaNumeric(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))


# Another Way

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = re.sub(r"[^a-z0-9]", "", s.lower())
        reversedString = ''.join(reversed(newString))
        if newString == reversedString:
            return True
        else:
            return False
