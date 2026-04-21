class Solution:
    def maxScore(self, s: str) -> int:

        s= list(map(lambda x:int(x),s))
        # print(s)
        sm=sum(s)
        z=res=0

        for i in range(len(s)-1):

            if s[i]:
                sm-=1
            else:
                z+=1

            res=max(res,sm+z)

        return res



        

        