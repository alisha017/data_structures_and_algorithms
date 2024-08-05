# https://leetcode.com/problems/valid-anagram/description/
# https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        if s == t:
            return True

        s_dict = defaultdict(int)

        for char in s:
            s_dict[char] += 1

        for char in t:
            if char not in s_dict:
                return False

            s_dict[char] -= 1
            if s_dict[char] == 0:
                s_dict.pop(char)

        if s_dict:
            return False

        return True
