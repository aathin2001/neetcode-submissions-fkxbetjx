class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res=0
        
        for l in range(len(s)):
            char={}
            maxf=0
            for r in range(l,len(s)):
                char[s[r]]=char.get(s[r],0) +1
                maxf=max(maxf,char[s[r]])
                if (r-l+1) - maxf <=  k :
                    res=max(res,r-l+1)

        return res
        