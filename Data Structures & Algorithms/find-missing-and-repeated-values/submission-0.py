class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        l=len(grid)
        chck=[0]*l*l
        # print(chck)
        for a in grid:
            for b in a:
                # print(b)
                chck[b-1]+=1
        res=[0]*2
        for i,j in enumerate(chck):
            
            if j >1 :
                res[0]=i+1

            elif j==0:
                res[1] = i+1

        return res