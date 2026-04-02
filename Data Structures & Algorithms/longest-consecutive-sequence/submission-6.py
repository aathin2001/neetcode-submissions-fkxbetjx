class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen=set(nums)
        c=0
        res=0
        for i in nums:
            c=1
            while True:
                if i+1 in seen:
                    c+=1
                else:
                    break

                i+=1

            res=max(res,c)

        return res



        