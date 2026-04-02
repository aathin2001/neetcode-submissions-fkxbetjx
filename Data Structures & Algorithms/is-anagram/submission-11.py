class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        b=[0]*26
        
        for i in range(len(s)):

            b[ord(s[i])-ord('a')]+=1
            b[ord(t[i])-ord('a')]-=1

        return b == [0]*26

        

        