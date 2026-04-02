class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        flag=False
        if sorted(s) == sorted(t):
            flag= not flag

        return flag