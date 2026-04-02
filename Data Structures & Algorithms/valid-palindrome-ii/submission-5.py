class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        # res=True
        if s == s[::-1]:
            return True
        else:
            l,r=0,len(s)-1
            while l<r:
                if s[l] != s[r]:
                    skipl,skipr=s[:l]+s[l+1:] , s[:r]+s[r+1:]
                    return skipl == skipl[::-1] or skipr == skipr[::-1]

                l+=1
                r-=1

            # return True

