class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        box = defaultdict(set)

        for x in range(0 , 9):
            for y in range(0 , 9):

                if board[x][y]=='.':
                    continue

                val = board[x][y]
                if val in rows[x] or val in cols[y] or val in box[(x//3,y//3)]:
                    return False

                rows[x].add(val)
                cols[y].add(val)
                box[(x//3, y//3)].add(val)
                
        return True