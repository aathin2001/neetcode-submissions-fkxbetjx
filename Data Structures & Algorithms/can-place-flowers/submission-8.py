class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        temp=[0]+flowerbed+[0]
        

        for i in range(1,len(flowerbed)+1):
            # print(temp[i-1],temp[i],temp[i+1])

            if temp[i-1] == temp[i] == temp[i+1] == 0:
                temp[i]= 1
                n-=1
            print(i,n)
            if not(n):
                break

            
        return n <= 0


        