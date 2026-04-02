class Solution:
    def reverseString(self, s: List[str]) -> None:
        temp=s.copy()
        l,r=0,len(s)-1

        while l<r:
            s[l]=temp[r]
            s[r]=temp[l]
            l+=1
            r-=1



        