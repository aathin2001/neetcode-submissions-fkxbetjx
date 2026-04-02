class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        c={}
        res=""

        if len(s) != len(t):
            return False


        for i in range(len(s)):

            if s[i] not in c and t[i] in c.values():
                break

            elif  s[i] not in c and t[i] not in c.values()   :
                c[s[i]] = c.get(s[i],t[i])

            res+= c[s[i]]

            if res != t[:i+1]:
                break

        return res == t