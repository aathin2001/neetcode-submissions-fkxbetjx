class Solution:
    def reverseString(self, s: List[str]) -> None:
        
        # l,r=0,len(s)-1


        for i in range(len(s)//2):
            l=i
            r=-(i+1)
            s[l],s[r]=s[r],s[l]
        