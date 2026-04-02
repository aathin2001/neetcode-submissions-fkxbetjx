class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        cmap={} #keyboard mapping  variable
        t=0     #time taken 
        f=0     #finger current position


        for  i,c in enumerate(keyboard):        #keyboard mapping 
            cmap[c] = i

        for i in word:              
            t+= abs(f-cmap[i])          #track the time per c
            f=cmap[i]                   #update curr position of the finger

        return t                    #return the time taken 

        