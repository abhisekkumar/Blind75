# https://leetcode.com/problems/group-anagrams/description/
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagram_dict = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord[c] - ord['a']] += 1
            count = tuple(count)

            if count in anagram_dict:
                anagram_dict[count].append(s)
            else:
                anagram_dict[count] = s
        return list(anagram_dict.values())