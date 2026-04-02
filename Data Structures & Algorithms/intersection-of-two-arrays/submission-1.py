class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        res=[]


        for i in set(nums2):
            if i in set(nums1):
                res.append(i)


        return res
        