class Solution:
    def maxDifference(self, s: str) -> int:
        c={}
        o,e=0,len(s)

        for i in s:
            c[i] = c.get(i,0)+1

        for i in c.values():
            if i%2:
                o=max(i,o)

            else:
                e=min(e,i)

        return o-e

        