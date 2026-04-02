class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Making sliding window check pots empty len(3) then midle pot ocupy


        temp=[0]+flowerbed+[0]  #making the optimal pattern

        for i in range(1,len(flowerbed)+1): #iterate through pots
            if n ==0 :
                break

            elif temp[i-1] == temp[i] == temp[i+1] == 0:
                temp[i] = 1
                n-=1


        return (n == 0)
            
            
            