class Solution:
    def minOperations(self, logs: List[str]) -> int:

        res=0

        for i in logs:
            if i=="../":
                res-=1
            elif i=="./":
                continue
            else:
                res+=1
            res=max(res,0)

        return res
        