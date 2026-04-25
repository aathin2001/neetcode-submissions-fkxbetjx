class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen=[]

        res=0

        for i in s:
            
            while i in seen:
                seen.pop(0)
                # j+=1

            seen.append(i)
            res=max(len(seen),res)

        return res

            




        
                    


        

            