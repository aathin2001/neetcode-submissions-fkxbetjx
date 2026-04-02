class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        temp=[]

        for i in matrix:
            temp.extend(i)
        
        print(temp)
        
        l,r=0,len(temp)-1

        while l <= r :
            m= r+l //2

            if temp[m] > target:
                r=m-1
            elif temp[m] < target:
                l = m+1
            elif temp[m] == target:
                return True

        return False
