class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        cont={}
        
        l=0
        res=0

        for i in range(len(s)):
            if s[i] in cont:
                l=max(cont[s[i]] + 1,l)


            cont[s[i]]=i
            res= max(res,i-l+1)

        return res




        
                    


        

            