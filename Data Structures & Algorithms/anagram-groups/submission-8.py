from collections import defaultdict;   # use for default type for  dictio
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res=defaultdict(list)         #by default values will be an list []

        for s in strs:
            indeces =[0] * 26         # create an map for storing all char in list for anagram check
            for c in s :
                indeces[ord(c)-ord('a')] += 1       #this one make hashmap key unique key for anagram char

            res[tuple(indeces)].append(s)           #append the anagram match 

        return list(res.values())                   #strs=["act","pots","tops","cat","stop","hat"]
                                                    #outpt :[["act","cat"],["pots","tops","stop"],["hat"]]
