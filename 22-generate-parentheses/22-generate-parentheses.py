class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res= []
        st = []
        def backtrack(open , close):
            if open ==close == n:
                res.append(''.join(st))

            # if open are less than n
            if open< n:
                st.append('(')
                backtrack(open+1 , close)
                st.pop()

            if open > close:
                st.append(')')
                backtrack(open, close+1)
                st.pop()

        backtrack(0 , 0)
        return(res)