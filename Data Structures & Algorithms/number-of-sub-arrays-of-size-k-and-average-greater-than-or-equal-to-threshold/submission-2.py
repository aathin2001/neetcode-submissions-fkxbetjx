class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res=0

        for i in range(len(arr)-k+1):
            a=sum(arr[i:k+i])/k
            
            if a>= threshold:
                res+=1

        return res