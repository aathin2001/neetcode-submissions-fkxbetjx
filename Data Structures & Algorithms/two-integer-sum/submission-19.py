class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        cnt={}

        for i in range(len(nums)):
            diff=target - nums[i]

            if diff in cnt:
                return [cnt[diff],i]
            else:
                cnt[nums[i]] =i

        

