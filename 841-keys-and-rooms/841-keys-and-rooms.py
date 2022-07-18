class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque([])
        q.append(rooms[0])

        unlocked = [0]
        

        while q:
            keys = q.popleft()

            for k in keys:
                if k not in unlocked:
                    q.append(rooms[k])
                    unlocked.append(k)


        if len(unlocked)!=len(rooms):
            return(False)
        
        return True
