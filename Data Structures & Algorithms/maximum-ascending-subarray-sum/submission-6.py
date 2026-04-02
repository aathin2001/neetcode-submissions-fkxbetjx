class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        nums=nums +[0]
        res=s=0

        for i in range(len(nums)-1):
            s+=nums[i]
            res=max(res,s)

            if nums[i] >= nums[i+1]:
                s=0

        return res

        

        