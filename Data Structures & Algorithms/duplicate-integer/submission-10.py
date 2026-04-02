class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        freq={}

        for i in nums:
            freq[i]=freq.get(i,0) +1

        return  any ( count >1 for count in freq.values() )
    
