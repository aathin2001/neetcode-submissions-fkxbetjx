class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result={}

        for i in strs:
            s = tuple(sorted(i))
            if s not in result:
                result[tuple(sorted(i))]=[i]
            else :
                result[tuple(sorted(i))].append(i)

        return list(result.values())

