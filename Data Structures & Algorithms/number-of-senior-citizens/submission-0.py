class Solution:
    def countSeniors(self, details: List[str]) -> int:
        
        c=0
        for i in details:
            age=int(i[11:-2])

            if age >60 :
                c+=1
            
        return c