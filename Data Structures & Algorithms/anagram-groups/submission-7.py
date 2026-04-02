class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        alph = "abcdefghijklmnopqrstuvwyxyz"
        res={}

        alph_map={ c:i for i,c in enumerate(alph) }

        for s in strs:
            indeces=[0] * len(alph)
            for c in s:
                indeces[alph_map[c]] += 1

            res[tuple(indeces)] = res.get(tuple(indeces),[]) +[s]
        
        return list(res.values())



