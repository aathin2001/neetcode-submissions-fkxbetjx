import collections 
from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        r = defaultdict(set)
        c = defaultdict(set)
        s = defaultdict(set)

        for row in range(len(board)):   #create and row index
            for column in range(len(board[row])):  #create column index

                value = board[row] [column]      #value of each row x column 0x0 or 0x1 like that

                if value == "." :           #skip the empty part
                    continue
                
                if value in r[row] or value in c[column] or value in s[row//3,column//3]:  # check if value already exist in dic
                    return False


                r[row].add(value)               #create an row dic
                c[column].add(value)            #create an column dic
                s[row//3,column//3].add(value)  #create an grid dic like squar in sudoku

        return True


        