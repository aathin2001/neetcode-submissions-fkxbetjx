class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        result=False
        for i in range(len(nums)):
            if nums[i] in nums[i+1::]:
                result=not result
                break
            
        return result
        