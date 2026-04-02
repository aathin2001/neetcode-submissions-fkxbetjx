class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        res=[0]*len(arr)
        m=arr[-1]
        
        for i in range(len(arr)):
            i=-(i+1)
            res[i]=m
            m=max(m,arr[i])

        res[-1]=-1

        return res




