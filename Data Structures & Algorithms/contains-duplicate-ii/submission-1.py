class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

                if len(nums) <= k:
                    return len(set(nums)) != len(nums)

                for i in range(0,len(nums)-k):
                    if len(nums[i:k+i+1]) != len(set(nums[i:k+i+1])):
                        return True

                return False
       