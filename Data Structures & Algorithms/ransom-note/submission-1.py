from collections import Counter 

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine) :
            return False

        ranNote=Counter(ransomNote)
        # print(ranNote)
        mag=Counter(magazine)

        for c in ranNote:
            if c not in mag or  ranNote[c] > mag[c]  :
                return False

        return True
