class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        res=s=nums[0]

        for i in range(1,len(nums)):

            if nums[i-1] < nums[i]:
                s+=nums[i]
            else:
                s=nums[i]
                

            res=max(res,s)

        return res
        