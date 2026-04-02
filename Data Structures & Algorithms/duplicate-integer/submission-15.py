class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

       uNums=set(nums)

       return len(nums) != len(uNums)



        