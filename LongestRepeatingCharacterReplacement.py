# https://leetcode.com/problems/longest-repeating-character-replacement/

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        char_freq = {}
        max_freq = 0
        result = 0

        for right in range(len(s)):
            char_freq[s[right]] = char_freq.get(s[right], 0) + 1
            max_freq = max(max_freq, char_freq[s[right]])

            if right - left + 1 - max_freq > k:
                char_freq[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)
        return result

        # left = 0
        # right = 0
        # char_freq = {}
        # result = 0
        #
        # while right < len(s):
        #     char_freq[s[right]] = char_freq.get(s[right], 0) + 1
        #     max_freq = max(char_freq.values())
        #
        #     if right - left + 1 - max_freq > k:
        #         char_freq[s[left]] -= 1
        #         left += 1
        #
        #     result = max(result, right - left + 1)
        #     right += 1
        #
        # return result
