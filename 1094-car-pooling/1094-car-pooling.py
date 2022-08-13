class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        d = defaultdict(int)


        for x,y,z in trips:
            d[y] += x
            d[z] -= x
    
    
    
        count = 0 

        for x in sorted(d):
            count+=d[x]
            if count > capacity:
                return(False)
            
        return True