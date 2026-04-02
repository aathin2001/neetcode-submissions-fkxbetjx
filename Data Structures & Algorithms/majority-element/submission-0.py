class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums) //2
        c={}

        for i in nums:

            c[i] = c.get(i,0)+1

            if c[i] > n:
                return i 
        