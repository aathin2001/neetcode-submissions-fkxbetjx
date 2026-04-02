class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        r=0

        while len(nums) != len(set(nums)):

            if nums[r] == nums[r+1]:
                nums.pop(r+1)
            else:
                r+=1

        return len(nums)

        
        







        