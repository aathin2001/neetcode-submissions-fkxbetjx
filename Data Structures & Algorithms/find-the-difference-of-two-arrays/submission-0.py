class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        res=[[],[]]

        n1=list(set(nums1))
        n2=list(set(nums2))

        for i in range(max(len(n1),len(n2))):
            if i<len(n1):
                if n1[i] not in n2:
                    res[0]+=[n1[i]]
                
            if i<len(n2):
                if n2[i] not in n1:
                    res[1]+=[n2[i]]

        return res

        