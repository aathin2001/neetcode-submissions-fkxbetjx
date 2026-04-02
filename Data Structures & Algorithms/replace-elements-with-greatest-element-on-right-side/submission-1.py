class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        res=[0]*len(arr) #creating an bucket
        m=arr[-1]   #last index value
        
        for i in range(len(arr)):   #iterate 0 - l
            i=-(i+1)                #0=> -1  to l => -l +1
            res[i]=m
            m=max(m,arr[i])         #max right index  value

        res[-1]=-1                  #last index to -1

        return res




