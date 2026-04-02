class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums=set(nums)
        l =0

        for i in nums:
            if i-1 not  in nums:
                streak = 1
                cur = i

                while cur+1 in nums:
                    cur += 1
                    streak +=1

                l = max(l,streak)

        return l     


        