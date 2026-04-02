class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        n= len(words)


        for i in range(n):
            for j in range(len(words[i])):
                if   j >=len(words) or i >=len(words[j]) or words[i][j] !=words[j][i]: # row and columns should be equal
                                        # and j < len(words[i])
                    return False

        return True