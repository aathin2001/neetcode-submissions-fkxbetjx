class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        num=[]

        # c=0

        for i in nums:

            if i:
                num.append(i)
    
                
        for i in range(len(nums)):

            if i < len(num):
                nums[i]=num[i]

            else:
                nums[i]=0

        

        
        