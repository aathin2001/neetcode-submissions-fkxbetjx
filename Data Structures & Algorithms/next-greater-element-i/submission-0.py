class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        c={i:j for j,i in enumerate(nums1)}
        res=[-1]*len(nums1)

        for i in range(len(nums2)):

            if nums2[i] in nums1:
                for j in range(i,len(nums2)):
                    if nums2[j] > nums2[i]:
                        res[c[nums2[i]]] = nums2[j]
                        break

        return res


        

        