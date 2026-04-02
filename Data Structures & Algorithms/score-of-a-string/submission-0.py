class Solution:
    def scoreOfString(self, s: str) -> int:
        res=0
        
        for i in range(len(s)-1):
            res+= max(ord(s[i]),ord(s[i+1])) - min(ord(s[i]),ord(s[i+1]))


        return res