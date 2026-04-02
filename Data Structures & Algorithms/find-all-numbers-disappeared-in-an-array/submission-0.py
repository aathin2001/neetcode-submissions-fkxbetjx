class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        res=[]

        for i in range(1,len(nums)+1):
            # print(i)
            if i not in nums:
                print(i)
                res.append(i)


        return res