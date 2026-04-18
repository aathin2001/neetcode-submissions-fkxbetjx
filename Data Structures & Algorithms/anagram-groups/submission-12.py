class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res={}


        for s in strs:
            tmp=[0]*26

            for c in s:
                tmp[ord('a')-ord(c)]+=1


            if tuple(tmp) not in res:
                res[tuple(tmp)]=list()

            res[tuple(tmp)].append(s)

        
        return list(res.values())

        