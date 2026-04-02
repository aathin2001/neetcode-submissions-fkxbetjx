from collections import defaultdict as dd
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row=dd(lambda : [0]*9)
        col=dd(lambda : [0]*9)
        sqr=dd(lambda : [0]*9)
        

        for r in range(9):
            for c in range(9):

                if board[r][c] == ".":
                    continue
                
                n=int(board[r][c]) -1

                row[r][n] +=1
                col[c][n] +=1
                sqr[(r//3,c//3)][n] +=1


                if row[r][n] >1 or col[c][n] >1 or sqr[(r//3,c//3)][n] >1:
                    return False

                
        return True