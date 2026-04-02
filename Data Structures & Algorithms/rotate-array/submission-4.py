class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        temp=nums[-k:]+nums[:-k]

        # nums=temp
        for i in range(len(temp)):
            nums[i]=temp[i]
         
        
       