class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        m={}

        for i in range(len(nums)):
            t=target - nums[i]
            if t in m :
                return [m[t],i]
            
            m[nums[i]] = m.get(nums[i],i)

