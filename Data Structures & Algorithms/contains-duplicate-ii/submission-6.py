class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        seen=set()
        l=0

        for i in range(len(nums)):
            # print (k)
            if nums[i] in seen:
                return True
            seen.add(nums[i])

            if i - l >= k:
                seen.remove(nums[l])
                l+=1

        
        return False