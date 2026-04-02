class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        n=0

        for i in range(len(s)):
            i=-(i+1)

            if s[i]== " ":
                return n

            n+=1        

        return n
        