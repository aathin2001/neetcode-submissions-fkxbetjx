class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res=dict()

        for w in strs:
            temp=[0]*26
            for c in w:
                temp[ord(c)-ord('a')]+= 1


            res[tuple(temp)]=res.get(tuple(temp),[])+[w]

        print(res)

        
        return list(res.values())