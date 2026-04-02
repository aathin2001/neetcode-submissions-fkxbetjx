class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums=set(nums)
        max_count=0

        for i in nums:
            n=i
            streaks=1

            while n+1 in nums:
                n+=1
                streaks+=1

            max_count=max(max_count,streaks)

        return max_count

        