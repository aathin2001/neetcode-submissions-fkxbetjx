class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # bucket=[0]*26
        anagram={}

        for s in strs:
            cmap=[0] *26
            for c in s:
                cmap[ord(c)-ord('a')] +=1

            anagram[tuple(cmap)] =anagram.get(tuple(cmap),[])+[s]

        print(anagram.values())

        return list(anagram.values())

        
