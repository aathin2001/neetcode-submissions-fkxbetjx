class Solution:
    def largestGoodInteger(self, num: str) -> str:

        f= False
        res=0

        for i in range(len(num)-2):

            if num[i] == num[i+1] == num[i+2]:
                f=True
                res=max(int(num[i]),res)

        a= str(res)*3 if f  else ""
        
        return a