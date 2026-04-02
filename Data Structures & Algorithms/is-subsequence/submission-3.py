class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        res= False
        
        p=0 #pointer 

        for  i in t:

            if p < len(s) and i == s[p]: #check the whether the i == pointer in s 
                p+=1      #then next letter

            if p == len(s):   #pointer reach the end of s return result
                res=True
                return res

            
        return res