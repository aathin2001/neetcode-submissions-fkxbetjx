class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        c={}


        for i,row in enumerate(words):
            for j,column in enumerate(row):
                c[j]=c.get(j,"")+column

        for i,word in enumerate(words):
            if word != c[i]:
                return False

        return True