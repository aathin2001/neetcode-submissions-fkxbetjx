class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        temp=[0]* len(grid) * len(grid)
        res=[0,0]

        for i in grid:
            for n in i:
                temp[n-1] +=1

        for i in range(len(temp)):
            
            if temp[i] > 1:
                res[0] = i+1
            if temp[i] ==0:
                res[1] = i+1
        
        return res