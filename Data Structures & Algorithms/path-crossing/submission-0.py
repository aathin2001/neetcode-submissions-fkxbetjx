class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        cor=[0,0]
        m={(0,0):1}

        for d in path:
            print(d)
            if d =="N":
                cor[1]+=1
            elif d == "S":
                cor[1]-=1
            elif d == "W":
                cor[0]+=1
            elif d == "E":
                cor[0]-=1

            m[tuple(cor)] =m.get(tuple(cor),0)+1
            print(cor)
            if m[tuple(cor)] >1:
                return True

        return False

