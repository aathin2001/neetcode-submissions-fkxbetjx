class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res=streak=0

        for i in nums:
            streak+=1

            if i == 0:
                streak=0

            res=max(res,streak)


        return res
        