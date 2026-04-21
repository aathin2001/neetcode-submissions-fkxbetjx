class Solution:
    def maxScore(self, s: str) -> int:
        
        res=z=sm=0
        for i in s:
            if i=="1":
                sm+=1
        print(sm)
       
        for i in range(len(s)-1):

            if int(s[i]):
                sm-=1
            else:
                z+=1

            res=max(res,sm+z)

        return res



        

        