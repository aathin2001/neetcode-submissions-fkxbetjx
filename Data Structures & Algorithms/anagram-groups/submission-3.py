from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result=defaultdict(list)


        for i in strs:
            sorted_s=tuple(sorted(i))
            result[sorted_s].append(i)
        
        return list(result.values())
