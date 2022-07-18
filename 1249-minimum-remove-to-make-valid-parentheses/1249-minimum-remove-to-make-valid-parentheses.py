class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        st = []
        delidx = []
        res = []
        out = ''
        for x in range(0 , len(s)):
            if s[x]==')':
                if st:
                    st.pop()
                else:
                    delidx.append(x)
            
            elif s[x]=='(':
                st.append([s[x], x])
    
            res.append(s[x])

        while st:
            delidx.append(st.pop()[1])

        for x in range(0 , len(res)):
            if x not in delidx:
                out+=res[x]

        return(out)