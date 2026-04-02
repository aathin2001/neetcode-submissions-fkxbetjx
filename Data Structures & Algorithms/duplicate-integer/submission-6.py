class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1 = sorted(nums)

        return  len(set(nums1)) !=  len(nums1)
        
