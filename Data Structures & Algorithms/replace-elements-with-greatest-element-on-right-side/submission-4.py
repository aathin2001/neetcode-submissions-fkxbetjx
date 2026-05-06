class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        tmp=arr.copy()
        h=arr[-1]

        for i in range(len(arr)):
            i=-(i+1)

            arr[i]=h

            h=max(h,tmp[i])

        arr[-1]=-1

        return arr



       
        