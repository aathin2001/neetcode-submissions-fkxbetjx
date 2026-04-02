class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        temp=[0]+flowerbed+[0]

        l,m,r = 0,1,2

        while r < len(temp) and n:

            if temp[l] == temp[m] == temp[r] == 0:
                temp[m] = 1
                n-=1

            l+=1
            m+=1
            r+=1

        return (n ==0)