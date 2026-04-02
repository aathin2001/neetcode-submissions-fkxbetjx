class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sbuc={}
        tbuc={}


        for i in range(len(s)):
            sbuc[s[i]]=sbuc.get(s[i],0)+1
            tbuc[t[i]]=tbuc.get(t[i],0)+1

        return sbuc == tbuc 

      

