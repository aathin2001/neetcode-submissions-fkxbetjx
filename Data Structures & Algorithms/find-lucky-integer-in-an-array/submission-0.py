class Solution:
    def findLucky(self, arr: List[int]) -> int:

        luckyNumber={}
        res=0

        for i in arr:
            luckyNumber[i] = luckyNumber.get(i,0)+1

        for i in luckyNumber:
            if luckyNumber[i] == i :
                res=max(res,i)

        a = res if res else -1
        
        return a

        