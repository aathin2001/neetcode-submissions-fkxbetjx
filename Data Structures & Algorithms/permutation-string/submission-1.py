class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1=sorted(s1)
        l=len(s1)
        res= False
        check=[]

        for i in range(0,len(s2)-l+1):
            if s2[i] in s1:
                c=s2[i:l+i]
                if sorted(c) == s1:
                    check += c
                    res= True
        
        return res




        
        