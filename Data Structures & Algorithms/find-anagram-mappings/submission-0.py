class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l=len(nums1)
        nmap={}
        res=[0] * l

        for i,num in enumerate(nums2):
            nmap[num] =i

        for i in range(l):
            res[i] = nmap[nums1[i]]

        return res


        