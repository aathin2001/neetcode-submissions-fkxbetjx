class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        
        char="balloon"
        cmap={}
        tmap={}
        res=len(text)

        for i in char:
            cmap[i]=cmap.get(i,0)+1

        for i in text:
            tmap[i]=tmap.get(i,0)+1

        for i in set(char):
            if i in tmap and cmap[i] <= tmap[i]:
                res=min(res,tmap[i]//cmap[i])
            else:
                return 0

        return res
            