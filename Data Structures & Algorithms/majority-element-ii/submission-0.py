class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        c={}
        l=len(nums)
        res=[]

        for i in nums:
            c[i] =c.get(i,0)+1

        for n in c:
            if c[n] > l//3 :
                print(n)
                res.append(n)


        return res
        