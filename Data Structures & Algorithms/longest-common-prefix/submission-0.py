class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        s=strs[0]
        res=len(s)

        for i in range(1,len(strs)):
            n=0
            for j in range(len(strs[i])):
        # print(j)
                if j>= len(s) or  strs[i][j] != s[j] :
                    break
                else:
                    n+=1
            res=min(res,n)
# print(s[:res],res)
        return s[:res]
            
        