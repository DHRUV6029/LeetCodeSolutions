class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visit = set({(0,0)})
        x =0 
        y =0

        for i in path:
            if i =='N':
                y+=1
            elif i=='E':
                x+=1
            elif i=='W':
                x-=1
            else:
                y-=1
    
            if (x,y) in visit:
                return(True)
        
            visit.add((x, y))

        return(False)