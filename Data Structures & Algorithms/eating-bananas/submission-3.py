import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r,res=1,max(piles),max(piles)

        while l<=r :
            rate=(l+r)//2
            t=0
            for b in piles:
                t+=math.ceil(b/rate)

            if t >h:
                l=rate+1
            elif t <=h:
                res=min(rate,res)
                r=rate-1

        return res
        
       
            
        