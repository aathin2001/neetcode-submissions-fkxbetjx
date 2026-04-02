class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        m={}
        res=-1

        for i in nums:
            m[i] = m.get(i,0)+1

        for i in m:
            if m[i] == 1:
                res=max(res,i)

        return res