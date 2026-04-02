class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        l=0
        char={}
        maxf=0
        for r in range(len(s)):
            
            char[s[r]] = char.get(s[r],0)+1
            maxf=max(maxf,char[s[r]])

            if r-l+1 - maxf >k :
                char[s[l]]-=1
                l+=1

            res=max(res,r-l+1)

        return res
            

        