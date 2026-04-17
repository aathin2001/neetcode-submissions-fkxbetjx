class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l,r=max(weights),sum(weights)

        res=r

        while l<=r:
            capacity=(l+r)//2
            i=ship=0
            d=1
            while i<len(weights):
                
                ship+=weights[i]
                if ship>capacity:
                    i-=1
                    ship=0
                    d+=1
        
                i+=1

            print(capacity,d)
            if d > days:
                l=capacity+1
            elif d<=days:
                res=min(res,capacity)
                r=capacity-1 

                    
        return res