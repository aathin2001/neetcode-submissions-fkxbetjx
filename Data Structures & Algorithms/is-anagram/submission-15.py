class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        tmp=[0]*26

        if len(s) != len(t):
            return False



        for i in range(len(s)):
            tmp[ord(s[i])-ord("a")]+=1
            tmp[ord(t[i])-ord("a")]-=1

        
        return tmp == [0]*26

