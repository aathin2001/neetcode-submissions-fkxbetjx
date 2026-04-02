class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        prevmap={}

        for i ,num in enumerate (numbers):
            diff = target - num

            if diff in prevmap:
                return [prevmap[diff]+1,i+1]

            prevmap[num]= i