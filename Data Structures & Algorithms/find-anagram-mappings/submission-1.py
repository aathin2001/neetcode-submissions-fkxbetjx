class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=len(nums1)
        nmap={}
        res=[]

        for i,num in enumerate(nums2):
            nmap[num] =i

        for i in nums1:
           res.append(nmap[i])

        return res


        