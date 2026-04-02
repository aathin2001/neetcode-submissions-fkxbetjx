class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        n=[0] * len(arr)
        m=arr[-1]

        for i in range(1,len(arr)+1):
            n[-i] = m
            m=max(m,arr[-i])
            print(m,arr[-i])

        n[-1]=-1
        return n
        