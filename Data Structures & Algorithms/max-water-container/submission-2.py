class Solution:
    def maxArea(self, heights: List[int]) -> int:

        res=0
        l,r=0,len(heights)-1


        while l<r:

            b=r-l
            h=min(heights[l],heights[r])
            # print(b,h)
            res=max(res,(b*h))

            if heights[r] > heights[l] :
                l+=1

            else:
                r-=1

            
        return res