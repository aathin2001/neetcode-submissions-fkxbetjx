class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        res=0
        streak=0
        for n in nums:

            if n :
                streak+=1
                res=max(res,streak)
            else:
                streak=0

            print(n,streak)

        return res

        