class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        res={}
        L=len(nums)+1

        l=r=s=0

        while r<len(nums):
            s+=nums[r]
            while s>=target:
                L=min(L,r-l+1)
                s-=nums[l]
                l+=1
                
            r+=1   
            

        L= 0 if L ==len(nums)+1 else L 
        
        return L