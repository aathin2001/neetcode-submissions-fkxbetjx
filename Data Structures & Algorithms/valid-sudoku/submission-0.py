import collections 
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        r = defaultdict(set)
        c = defaultdict(set)
        s = defaultdict(set)

        for row in range(len(board)):
            for column in range(len(board[row])):

                value = board[row] [column]

                if value == "." :
                    continue
                
                if value in r[row] or value in c[column] or value in s[row//3,column//3]:
                    return False


                r[row].add(value)
                c[column].add(value)
                s[row//3,column//3].add(value)

        return True


        