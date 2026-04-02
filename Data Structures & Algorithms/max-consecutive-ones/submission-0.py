class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        res=0
        p1=c=0

        while p1 < len(nums):

            if nums[p1] != 1 :
                c=0
            else:
                c+=1
            
            res=max(res,c)

            p1+=1

        return res