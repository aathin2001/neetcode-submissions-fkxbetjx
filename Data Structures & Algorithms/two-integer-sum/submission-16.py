class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        n={}

        for i in range(len(nums)):
            t=target - nums[i]

            if t in n:
                return [n[t],i]

            n[nums[i]]=n.get(nums[i],i)




        