class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        
        res=streak=0

        for i in range(len(s)):

            if streak < len(t) and s[i]== t[streak]:
                streak+=1
            

            res=max(res,streak)

        return len(t[res:])


        