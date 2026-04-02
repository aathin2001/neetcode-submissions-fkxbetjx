class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:

        res=s= nums[0]
        # s=0

        for i in range(1,len(nums)):

            if nums[i] <= nums[i-1]:
                s=0
                

            s+=nums[i]
            res=max(res,s)

        return res
        