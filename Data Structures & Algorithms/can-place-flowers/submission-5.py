class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Making sliding window check pots empty len(3) then midle pot ocupy


        temp=[0]+flowerbed+[0]  #making the optimal pattern

        for i in range(1,len(flowerbed)+1): #iterate through pots
            if n ==0 :
                break

            elif temp[i-1] == temp[i] == temp[i+1] == 0: # sliding window to check empty 3 pots
                temp[i] = 1                                #asighn the midle pot 
                n-=1                                        #reduce flower


        return (n == 0)                 # return is flower is
            
            
            