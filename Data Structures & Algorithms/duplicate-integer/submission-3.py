class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result= False
        for i in range(0,len(nums)):
            if nums[i] in nums[i+1::]:
                return True 
                break
        return result