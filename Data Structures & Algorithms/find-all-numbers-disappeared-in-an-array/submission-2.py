class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dupe=set(nums)
       
        chck=[False] * len(nums)

        for num in nums:
            chck[num-1] = True

        res=[]
        for i in range(len(chck)):
            if not(chck[i]):
                res.append(i+1)

        return res