class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res=0
        s=0
        c={0:1}


        for n in nums:
            s+=n
            diff=s-k

            res+=c.get(diff,0)
            c[s]=c.get(s,0)+1

        return res
