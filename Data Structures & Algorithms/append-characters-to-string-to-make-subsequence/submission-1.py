class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        i=j=m=0
        

        while i<len(s) and j <len(t): # two condition pointer limit

            if s[i] == t[j] :         # check substring
                j+=1

            i+=1

           
        return len(t) - j             #return length of string to form subsequence



        