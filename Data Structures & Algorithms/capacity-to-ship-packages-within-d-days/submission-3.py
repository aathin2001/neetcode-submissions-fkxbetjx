class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        l,r=max(weights),sum(weights)

        res=r

        while l<=r:
            capacity=(l+r)//2
            ship=1
            cur_capacity=0
            for w in weights:
                cur_capacity+=w
                if cur_capacity > capacity:
                    cur_capacity=w
                    ship+=1
                
                 
            

            # print(capacity)
            if ship > days:
                l=capacity+1
            elif ship<=days:
                res=min(res,capacity)
                r=capacity-1 

                    
        return res