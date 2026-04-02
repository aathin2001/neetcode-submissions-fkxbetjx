class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        freq={}

        for i in nums:
            if i in freq:
                freq[i]+= 1

            else :
                freq[i] = 1

        return  any ( count >1 for count in freq.values() )
    
