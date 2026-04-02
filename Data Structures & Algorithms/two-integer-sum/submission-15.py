class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c={}
        res=[]

        for  i in range(len(nums)):
            t=target - nums[i]

            if t in c:
                n=[c[t],i]
                return n

            c[nums[i]] = c.get(nums[i],i)