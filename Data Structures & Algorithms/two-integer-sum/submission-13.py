class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indeces ={}         # store the number : index(last occured)

        for i,num in enumerate(nums):       # generate i =>index , num=>number
            indeces[num]=i                  # create an hashmap number(key):index(value)

        for i,num in enumerate (nums):
            diff= target - num

            if diff in indeces and indeces[diff] != i:      #check wether the diff in nums and not the same index number 
                return [i,indeces[diff]]