# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        hashSet = set()
        result, i, j = 0, 0, 0

        while i < len(s) and j < len(s):
            if s[j] not in hashSet:
                hashSet.add(s[j])
                j += 1
                result = max(result, j - i)
            else:
                hashSet.remove(s[i])
                i += 1
        return result




