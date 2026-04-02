class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res={}

        for i in strs:
            b=[0]*26
            for j in i:
                b[ord(j)-ord("a")] +=1

            res[tuple(b)] = res.get(tuple(b),[])+[i]


        return list(res.values())

        
        