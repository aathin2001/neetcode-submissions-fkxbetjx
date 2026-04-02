import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # rate=list(range(1,max(piles)+1))
        l,r=1,max(piles)
        res=max(piles)
        #[1,2,3,4,5]

        while l<=r:
            k=0
            m=(l+r) //2

            for b in piles:
                k+= math.ceil(b/m)

            if k <= h:
                r=m-1
                res=min(res,m)
            elif k > h:
                l=m+1

        return res
            
            
        