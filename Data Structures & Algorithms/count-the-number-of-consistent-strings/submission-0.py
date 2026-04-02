class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res=len(words)
        seen=set(allowed)
        for w in words:

            for c in w:
                if c not in seen:
                    res-=1
                    break


            


        return res
        