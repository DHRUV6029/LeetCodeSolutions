class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st = []

        def GetStackState(val_to_pop , st, pushed):
            if not st and pushed:
                st.append(pushed.pop(0))
            while st[-1] != val_to_pop and pushed:
                st.append(pushed.pop(0))
            if st[-1]==val_to_pop:
                st.pop()

        while pushed or popped:
            val_to_pop = popped.pop(0)
    
            GetStackState(val_to_pop, st, pushed)

        if st:
            return(False)
        
        return True
