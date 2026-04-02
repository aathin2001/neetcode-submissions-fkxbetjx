class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        i=j=0

        while i < len(word) and j < len(abbr):

            if word[i] == abbr[j]:
                i,j=i+1,j+1

            elif abbr[j].isalpha() or abbr[j] == "0":
                print(abbr[j])
                return False

            elif not(abbr[j].isalpha()):
                n=""
                while j< len(abbr) and not(abbr[j].isalpha()):
                    n+=abbr[j]
                    j+=1

                i+=int(n)

        # print(i,j)

        return (i == len(word)and j == len(abbr))


        
        