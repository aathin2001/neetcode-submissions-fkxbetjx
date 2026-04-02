class Solution:
    def firstUniqChar(self, s: str) -> int:

        cnt={}
        # res=len(s)
        # flag=False
        for i in range(len(s)):
            cnt[s[i]] = cnt.get(s[i],[])+[i]

        for i in s:
            if len(cnt[i]) == 1:
                return cnt[i][0]

        return -1
        