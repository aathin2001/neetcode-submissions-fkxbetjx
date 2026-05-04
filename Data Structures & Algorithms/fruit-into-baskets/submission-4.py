class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        basket={}
        l=r=0
        res=0

        while r < len(fruits):

            basket[fruits[r]]=basket.get(fruits[r],0)+1
            while len(basket)>2:
                basket[fruits[l]]-=1
                if basket[fruits[l]]==0:
                    basket.pop(fruits[l])
                l+=1   


            res=max(res,r-l +1 )    
            r+=1       


        return res