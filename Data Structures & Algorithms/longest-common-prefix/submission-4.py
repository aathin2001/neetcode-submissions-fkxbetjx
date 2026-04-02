class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""

        for i in range(len(strs[0])):   # 1st index word as an refernce 
            for j in strs:              # iterate through each words in list

                if i == len(j) or j[i] != strs[0][i]:       #return res when the word bound end or reference letter mismatch
                    return res
                    # break
            
            res+=strs[0][i]         #append the matched letter
            
        return res