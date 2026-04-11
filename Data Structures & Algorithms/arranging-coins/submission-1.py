class Solution:
    def arrangeCoins(self, n: int) -> int:
        res=n
        l,r=1,n

        while l<=r:
            m=(l+r)//2
            m1=(m/2) * (m+1)

            if m1 >= n:
                res=min(res,m)
                r=m-1
                if m1 ==  n:
                    return m
            elif m1 < n:
                l=m+1


        return res -1



        
        