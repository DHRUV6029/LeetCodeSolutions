class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtrack(s=1  , cur=[]):
            #base case
            if len(cur)==k:
                res.append(cur[:])

            for x in range(s, n+1):
                cur.append(x)
                backtrack(x+1 , cur)
                cur.pop()


        backtrack()

        return(res)
