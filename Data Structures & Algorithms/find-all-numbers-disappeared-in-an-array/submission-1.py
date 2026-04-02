class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dupe=set(nums)
        res=[]

        for i in range(1,len(nums)+1):
            # print(i)
            if i not in dupe:
                print(i)
                res.append(i)


        return res