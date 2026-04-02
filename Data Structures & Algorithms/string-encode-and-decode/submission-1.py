from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        var1 = ''
        for i in strs:
            var1 += str(len(i)) + '#' + i
        return var1

    def decode(self, s: str) -> List[str]:
        var2 = []
        i = 0
        while i < len(s):
            # find the number before "#"
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])   # number before "#"
            word = s[j+1 : j+1+length]  # extract word of 'length'
            var2.append(word)
            i = j + 1 + length   # move pointer
        return var2
