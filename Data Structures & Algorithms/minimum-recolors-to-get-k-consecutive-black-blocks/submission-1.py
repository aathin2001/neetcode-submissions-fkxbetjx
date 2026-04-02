class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        
        c={'W':0,
        'B':0}
        res=len(blocks)
        l=0

        for i in range(len(blocks)):
            c[blocks[i]] +=1
            print(blocks[l:i])
            print(c)

            if i-l >= k:
                c[blocks[l]] -=1
                l+=1

            if c['W'] +c['B'] == k:
                res=min(res,c['W'])

        return res