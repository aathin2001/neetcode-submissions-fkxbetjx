class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prev_map ={}         # we append the key untill we reach the diff value

        for i,num in enumerate(nums):
            diff = target -num          #1.create  an posible number to get the target (num=3 , diff =4 )

            if diff in prev_map :       #3 .filter the first posible number 
                return [prev_map[diff],i]

            prev_map[num]=i             #2.append the hash map untill the above condition satisfy