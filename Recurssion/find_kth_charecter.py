"""
Input: k = 5

Output: "b"

Explanation:

Initially, word = "a". We need to do the operation three times:

Generated string is "b", word becomes "ab".
Generated string is "bc", word becomes "abbc".
Generated string is "bccd", word becomes "abbcbccd"    

"""

class Solution:
    def kthCharacter(self, k: int) -> str:
        def generate_string(s):
            new_str = ""
            for ch in s:
                new_str += 'a' if ch=='z' else chr(ord(ch) + 1)
            return new_str
        s = 'a'
        while len(s)<k:
            s+=generate_string(s)
        return s[k-1]