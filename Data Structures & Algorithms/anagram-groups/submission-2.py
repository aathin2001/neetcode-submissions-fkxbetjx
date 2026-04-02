from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        my_dict=defaultdict(list)

        for i in strs:
            key=tuple(sorted(i))
            my_dict[key].append(i)

        return list(my_dict.values())

