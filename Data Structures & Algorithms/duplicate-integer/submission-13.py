class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        c={}

        for i in nums:
            c[i] =c.get(i,0)+1

            if c[i] > 1:
                return True

        return False
        

        