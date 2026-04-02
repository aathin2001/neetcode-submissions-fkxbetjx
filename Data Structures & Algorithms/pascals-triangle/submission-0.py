class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[[1]]


        for i in range(1,numRows):
            n=[0]+res[-1]+[0]
            a=[]
            l=0
            r=1
            while r <len(n):
                a.append(n[l]+n[r])
                l+=1
                r+=1

            res.append(a)

        return res

            
        