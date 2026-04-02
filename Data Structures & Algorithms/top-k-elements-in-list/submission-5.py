class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        c={}
        res=[]
        res2=[]

        for i in nums:
            c[i] =c.get(i,0)+1

        for n in c:
            res.append([c[n],n])

        res.sort(reverse=True)

        for n in range(k):
            res2.append(res[n][1])

        return res2




          
        