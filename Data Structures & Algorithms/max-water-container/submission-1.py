class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area=0
        r = 0
        l = len(heights)-1

        while r < l :
            n_area = min(heights[r],heights[l]) * (l-r)
            max_area = max(max_area,n_area)
            if heights[r] == heights[l]:
                if heights[r+1] > heights[l-1]:
                    l-= 1
                else :
                    r+=1
            else :
                if heights[r] > heights[l]:
                    l-=1
                else:
                    r+=1

        return max_area
        