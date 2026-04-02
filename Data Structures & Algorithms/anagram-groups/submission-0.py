class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        valid={tuple(sorted(d)) for d in strs }
        result=[]

        for i in valid:
            res=[]
            for j in strs:
                if i == tuple(sorted(j)):
                    res.append(j)

            result.append(res)


        return result