class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        c=0
        for i in s[::-1].strip():
            print(i)
            if i== " ":
                return c
            c+=1
        
        return c