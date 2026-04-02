class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r=0,len(s)-1
        res=True
        
        
        while l<r:
            if s[l] != s[r]:
                skipl,skipr=s[:l]+s[l+1:] , s[:r]+s[r+1:]
                return skipl == skipl[::-1] or skipr == skipr[::-1]

            l+=1
            r-=1

        return True

