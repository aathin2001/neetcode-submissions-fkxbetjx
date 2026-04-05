class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        x=y=0
        m={(0,0):1}

        loc=set()
        loc.add((0,0))

        dir={
            "N" :[0,1],
            "S" :[0,-1],
            "W" :[1,0],
            "E" :[-1,0]
        }

        for d in path:
            

            dx,dy = dir[d]

            x,y =x+dx , y+dy
            
            # print(x,y)
            # print(loc)

            if tuple([x,y]) in loc:
                return True
            loc.add(tuple([x,y]))

        return False
       
