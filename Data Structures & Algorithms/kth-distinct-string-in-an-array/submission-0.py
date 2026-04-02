class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        c={}

        for i in arr:

            c[i] =c.get(i,0)+1

        for i in c:

            if c[i] ==1:
                k-=1

            if k == 0:
                return i

        return ""
        
       