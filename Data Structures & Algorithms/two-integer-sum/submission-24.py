class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        c={}

        for i in range(len(nums)):
            diff=target-nums[i]

            if diff in c:
                return [c[diff],i]

            c[nums[i]]=i
            

           
        