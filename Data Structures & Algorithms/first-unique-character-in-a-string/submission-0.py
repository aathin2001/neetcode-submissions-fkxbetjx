class Solution:
    def firstUniqChar(self, s: str) -> int:

        cnt={}
        res=len(s)
        flag=False
        for i in range(len(s)):
            cnt[s[i]] = cnt.get(s[i],[])+[i]

        for i in cnt.values():
            if len(i) == 1:
                res=min(res,i[0])
                flag=True
            
        a=res if flag else -1

        return a
        